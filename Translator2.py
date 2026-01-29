import streamlit as st
from deep_translator import GoogleTranslator
import random

# -----------------------------
# CONFIGURATION
# -----------------------------
DEFAULT_SOURCE = "english"
DEFAULT_TARGET = "french"

st.set_page_config(
    page_title="Language Translator",
    page_icon="🌍",
    layout="wide",
)

# -----------------------------
# CUSTOM STYLING (UI THEME)
# -----------------------------
st.markdown(
    """
    <style>
    .main {
        background-color: #f6f8fa;
    }
    textarea {
        font-size: 16px !important;
    }
    .stButton button {
        background-color: #2c7be5;
        color: white;
        border-radius: 8px;
        padding: 0.6em 1.5em;
        font-weight: 600;
    }
    .stButton button:hover {
        background-color: #1a5fd0;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# HEADER
# -----------------------------
st.title("🌍 Language Translator")
st.caption("Fast, simple text translation powered by Google Translator")

#--------------------------------
#SIDEBAR
#------------------
st.sidebar.header("🕘 Translation History")


if "history" not in st.session_state:
    st.session_state.history = []

if not st.session_state.history:
    st.sidebar.caption("No translations yet — your first one will show up here 👀")

for item in reversed(st.session_state.history):
    with st.sidebar.expander(f"{item['from']} → {item['to']}"):
        st.write("**Input:**")
        st.write(item["input"])
        st.write("**Output:**")
        st.write(item["output"])

# -----------------------------
# LOAD LANGUAGES
# -----------------------------
translator = GoogleTranslator(source=DEFAULT_SOURCE, target=DEFAULT_TARGET)
languages = translator.get_supported_languages(as_dict=True)
language_names = sorted(languages.keys())

# -----------------------------
# LANGUAGE SELECTION
# -----------------------------
col1, col2, col3 = st.columns([4, 1, 4])

if "history" not in st.session_state:
    st.session_state.history = []

with col1:
    source_language = st.selectbox(
        "From",
        language_names,
        index=language_names.index(DEFAULT_SOURCE)
    )

with col2:
    st.markdown("<h2 style='text-align:center;'>➡️</h2>", unsafe_allow_html=True)

with col3:
    target_language = st.selectbox(
        "To",
        language_names,
        index=language_names.index(DEFAULT_TARGET)
    )

# -----------------------------
# TEXT INPUT / OUTPUT
# -----------------------------
left, right = st.columns(2)

with left:
    source_text = st.text_area(
        "Enter text to translate",
        height=250,
        placeholder="Type or paste text here..."
    )

with right:
    translated_text_placeholder = st.empty()

MAX_CHARS = 5000
char_count = len(source_text)

char_count = len(source_text)

if char_count == 0:
    st.caption("Quiet so far… 👀")
elif char_count < 50:
    st.caption("Short and sweet ✨")
elif char_count < 200:
    st.caption("Okay, we’re cooking now 🍳")
else:
    st.caption("📜 That’s a whole paragraph!")


st.caption(f"{char_count} / {MAX_CHARS} characters")

# -----------------------------
# TRANSLATE ACTION
# -----------------------------
if st.button("Translate"):
    # ---- Input Validation ----
    if not source_text.strip():
        st.error("❌ Please enter text to translate.")
    elif source_language == target_language:
        st.error("❌ Source and target languages must be different.")
    else:
        try:
            translator.source = languages[source_language]
            translator.target = languages[target_language]

            translation = translator.translate(source_text)

            translated_text_placeholder.text_area(
                "Translated text",
                translation,
                height=250
            )

        except Exception as e:
            st.error(f"⚠️ An unexpected error occurred: {e}")

    SUCCESS_MESSAGES = [
    "✨ Nailed it!",
    "🌍 Language barrier officially broken.",
    "🧠 Your multilingual era begins.",
    "📖 Translation complete!"
    ]
    st.success(random.choice(SUCCESS_MESSAGES))

    st.session_state.history.append({
    "from": source_language,
    "to": target_language,
    "input": source_text,
    "output": translation
})


# -----------------------------
# FOOTER
# -----------------------------
st.markdown("---")
st.caption("LingoBridge, Helping Conversations Cross Borders 🌍")
