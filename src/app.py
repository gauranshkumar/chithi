# Imports
import streamlit as st
import markdown
from streamlit_ace import st_ace, LANGUAGES, THEMES
import time
from mailer import Mailer
from info import get_server_info

# Utility Functions


def mail():
    '''Function to send the mail'''
    mailer.send_mail(to=recipients, bcc=bcc, subject=subject,
                     body=body, attachments=attachments)
    with st.spinner("Sending..."):
        time.sleep(5)
        st.success("Mail sent successfully!")


# Title for page
st.title("✉️ CHITTHI")
st.subheader("Send emails in Bulk ⚡")
st.markdown("*****")

# Takinks Mail ID and password of the Sender
st.markdown("##### Who's sending the mail? 🤔")
mailid = st.text_input("Email:")
passwrd = st.text_input("Password:", type="password")

# Choosing the server of sender
server = st.selectbox("Choose your Mail Provider", [
    "Gmail", "Yahoo", "Outlook", "Hotmail", "iCloud"])


# Some important info to setup the account
st.warning(get_server_info(st.session_state.get("server", server)))

# Collecting Recipients information
st.markdown("""*****
# Tell me about recipients ✨""")
recipients = st.text_input("Recipient:")
bcc = st.text_input("Bcc: \t")
st.info("Comma separated Id's")

# TODO: Allow option for reading recipients from CSV/XSLX file


# Taking Message to Mail in Markdown
st.markdown("""*****
# What's the message? 🔥""")

subject = st.text_input("Subject:")
# Setting split view for live Output of Markdown
col1, col2 = st.columns(2)
body = col1.text_area("Body:", height=300)
# body = st_ace(language=LANGUAGES[90], theme=THEMES[13], auto_update=True)
col2.markdown(st.session_state.get("body", body), unsafe_allow_html=True)

# If user wants to see the markdown eqivalent HTML Code
view_html = st.checkbox("View Raw HTML")
if view_html:
    st.code(markdown.markdown(st.session_state.get("body", body)))

st.info(
    """We support Markdown Editor 🎉 If you are new to Markdown check this [Guide](https://www.markdownguide.org/basic-syntax/).""")


# Attachments options for mail
attachments = st.file_uploader("Attachments:", accept_multiple_files=True)

# Calling the core Mailer Class
mailer = Mailer(mailid, passwrd, server.lower())


st.markdown("<br>", unsafe_allow_html=True)
# Sending the mail on Button Press
st.button("Send 📮", on_click=mail)
# TODO: Handle Alert if Mail not sent successfully

# Footer
st.markdown("""
<br><br>
<center> Made with ❤️ by <a href="https://gauranshkumar.github.io/" target="_blank">Gauransh Kumar</a> in 🇮🇳 </center>
""", unsafe_allow_html=True)
