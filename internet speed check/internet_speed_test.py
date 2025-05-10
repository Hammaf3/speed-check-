import streamlit as st
import speedtest

def test_speed():
    st.write("Running speed test...")
    st.text("Please wait while the test completes.")

    speed = speedtest.Speedtest()
    speed.get_best_server()

    download_speed = speed.download() / 1_000_000  # Convert to Mbps
    upload_speed = speed.upload() / 1_000_000  # Convert to Mbps
    ping = speed.results.ping

    return download_speed, upload_speed, ping

# Streamlit UI
st.title("Internet Speed Test")
st.write("Check your internet speed, including download and upload rates, as well as ping.")

if st.button("Run Speed Test"):
    try:
        download_speed, upload_speed, ping = test_speed()
        st.success("Speed Test Complete!")

        st.metric(label="Download Speed", value=f"{download_speed:.2f} Mbps")
        st.metric(label="Upload Speed", value=f"{upload_speed:.2f} Mbps")
        st.metric(label="Ping", value=f"{ping:.2f} ms")
    except Exception as e:
        st.error(f"An error occurred while running the speed test: {e}")
else:
    st.info("Click the button above to start the speed test.")
