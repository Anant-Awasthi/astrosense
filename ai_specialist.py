def generate_ai_briefing(metrics, risk_score):
    """Generates automated AI Mission Specialist briefing."""
    kp = metrics["kp_index"]
    wind = metrics["solar_wind_speed"]
    
    if risk_score > 70 or kp >= 6.0:
        status = "NO-GO 🔴"
        recommendation = (
            "High solar radiation and elevated geomagnetic activity detected. "
            "High risk of satellite communications disruption and avionics single-event upsets (SEUs)."
        )
        action = "Delay launch window by at least 6 hours until geomagnetic storming subdues."
    elif 40 <= risk_score <= 70 or kp >= 4.0:
        status = "CAUTION 🟡"
        recommendation = (
            "Moderate space weather disturbances present. Solar wind speeds elevated. "
            "Primary flight telemetry will remain functional, but high-frequency radio blackouts are possible."
        )
        action = "Proceed with caution. Keep secondary backup telemetry systems on standby."
    else:
        status = "GO FOR LAUNCH 🟢"
        recommendation = (
            "Space weather conditions are within nominal safety thresholds. "
            "Minimal solar flux and low geomagnetic activity."
        )
        action = "All orbital parameters clear. Proceed with launch sequence."
        
    return {
        "status": status,
        "recommendation": recommendation,
        "action": action
    }