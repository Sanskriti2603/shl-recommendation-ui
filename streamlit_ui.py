import streamlit as st
import requests

st.set_page_config(page_title="SHL Assessment Recommender", layout="wide")
st.title("SHL Assessment Recommendation System using RAG ( Kindly wait upto 1 minute as it is deployed on free tier server for backend response")

# Input area
query = st.text_area("Describe the role or requirement:", 
                     "Looking for an entry-level customer service test under 30 minutes...")

if st.button("Get Recommendations"):
    with st.spinner("Fetching recommendations..."):
        try:
            response = requests.post(
                "https://shl-recommendation-system-1lxo.onrender.com/recommend",
                json={"text": query}
            )
            if response.status_code == 200:
                results = response.json()["recommendations"]
                if results:
                    st.success(f"Top {len(results)} recommendations:")
                    for r in results:
                        st.markdown(f"""
                        #### [{r['Assessment Name']}]({r['URL']})
                        - ⏱️ Duration: **{r['Duration']} mins**
                        - 🌐 Remote Testing: **{r['Remote Testing Support']}**
                        - 🎯 Adaptive/IRT: **{r['Adaptive/IRT Support']}**
                        - 🧪 Test Types: {r['Test Type(s)']}
                        ---
                        """)
                else:
                    st.warning("No recommendations found.")
            else:
                st.error("API error. Check if backend is running.")
        except Exception as e:
            st.error(f"Error: {e}")
