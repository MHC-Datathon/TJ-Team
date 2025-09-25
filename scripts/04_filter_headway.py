import pandas as pd
from pathlib import Path

ROUTES = ["M101", "M102", "M103", "M2", "M3", "M4", "M15", "M15+", "M60+", "M100"]

INPUT = [
    Path("data_raw/MTA_Bus_Wait_Assessment__2020_-_2024_20250924.csv"),
    Path("data_raw/MTA_Bus_Wait_Assessment__Beginning_2025.csv")
]

OUT_PATH = Path("data_work/wait_assessment_clean.parquet")
OUT_PATH.parent.mkdir(parents=True, exist_ok=True)

ADD_ACE_LABELS = True
ACE_ROUTES_CSV = Path("data_raw/MTA_Bus_Automated_Camera_Enforced_Routes__Beginning_October_2019_20250921.csv")
WARNING_DAYS = 60

def _ci_col(df: pd.DataFrame, name_guess: str) -> str:
    # case insensitive col finder
    target = name_guess.lower()
    for c in df.columns:
        if c.lower() == target:
            return c
    raise KeyError(f"Column '{name_guess}' not found (case=insensitive)")

def load_one(path: str) -> pd.DataFrame:
    # load one WA file keep ALL original cols, add helpful features
    df = pd.read_csv(path, low_memory=False)

    # locate key cols
    month_col = _ci_col(df, "month")
    route_col = _ci_col(df, "route_id")
    passed_col = _ci_col(df, "number_of_trips_passing_wait")
    sched_col = _ci_col(df, "number_of_scheduled_trips")
    wa_col = _ci_col(df, "wait_assessment")
    period_col = _ci_col(df, "period")

    # filter to routes of interest
    df = df[df[route_col].isin(ROUTES)].copy()

    # add derived helpers
    df["month_dt"] = pd.to_datetime(df[month_col], errors="coerce")
    # % form for easier plotting
    df["wait_assessment_pct"] = (pd.to_numeric(df[wa_col], errors="coerce") * 100).round(2)
    # failing trips = scheduled - passing
    df["trips_failing_wait"] = (
        pd.to_numeric(df[sched_col], errors="coerce")
        - pd.to_numeric(df[passed_col], errors="coerce")
    ).clip(lower=0)

    # normalize period capitalization to reduce chart duplication
    df["period_norm"] = df[period_col].astype(str).str.title()

    return df

def add_ace_labels(df: pd.DataFrame) -> pd.DataFrame:
    # add ace_status using ace (NOT ABLE)
    ace = pd.read_csv(ACE_ROUTES_CSV)
    #case-insensitive locate needed columns
    route_col = _ci_col(ace, "Route")
    program_col = _ci_col(ace, "Program")
    impl_col = _ci_col(ace, "Implementation Date")

    # keep ACE only (exclude ABLE)
    ace = ace[ace[program_col].astype(str).str.upper().eq("ACE")].copy()
    ace["ace_start_date"] = pd.to_datetime(ace[impl_col], errors="coerce")

    # join key: route_id in WA vs route in ace
    wa_route_col = _ci_col(df, "route_id")
    key = ace[[route_col, "ace_start_date"]].dropna()
    key = key.rename(columns={route_col: wa_route_col})

    out = df.merge(key, on=wa_route_col, how="left")

    # month-level boundaries based on month_dt
    out["month_start"] = out["month_dt"]
    out["month_end"] = out["month_dt"] + pd.offsets.MonthEnd(0)

    def label_row(r):
        start = r["ace_start_date"]
        if pd.isna(start) or pd.isna(r["month_start"]):
            return "no_ace"
        warn_end = start + pd.Timedelta(days=WARNING_DAYS) # first 60 days
        if r["month_end"] < start:
            return "pre_ace"
        if r["month_start"] >= warn_end:
            return "post_ace"
        return "warning"
    
    out["ace_status"] = out.apply(label_row, axis=1)
    return out

def main():
    frames = []
    for file in INPUT:
        print(f"[INFO] Reading {file}")
        frames.append(load_one(file))
    wa = pd.concat(frames, ignore_index=True)
    print(f"[INFO] Combined rows: {len(wa):,}")

    if ADD_ACE_LABELS:
        print("[INFO] Adding ACE pre/warning/post labels...")
        wa = add_ace_labels(wa)

    wa.to_parquet(OUT_PATH, index=False)
    print(f"[DONE] Saved {len(wa):,} rows -> {OUT_PATH}")

    # Quick peeks
    try:
        print("\n[Route counts]")
        print(wa[_ci_col(wa, "route_id")].value_counts())
    except Exception:
        pass

    if "ace_status" in wa.columns:
        print("\n[ACE status counts]")
        print(wa["ace_status"].value_counts())

    
if __name__ == "__main__":
    main()