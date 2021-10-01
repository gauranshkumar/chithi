# Imports
<<<<<<< HEAD
import pandas as pd
import streamlit as st
import markdown
import mimetypes

=======
import streamlit as st
import markdown
>>>>>>> 31963c2eef02ca384c1efb486a4246cffbd4c1ba
# from streamlit_ace import st_ace, LANGUAGES, THEMES
import time
from mailer import Mailer
from info import get_server_info
<<<<<<< HEAD


=======

# Utility Functions


def mail():
    '''Function to send the mail'''
    mailer.send_mail(to=recipients, bcc=bcc, subject=subject,
                     body=body, attachments=attachments)
    with st.spinner("Sending..."):
        time.sleep(5)
        st.success("Mail sent successfully!")


>>>>>>> 31963c2eef02ca384c1efb486a4246cffbd4c1ba
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
c1, c2 = st.columns(2)
cc = c1.text_input("Cc")
cc = cc.split(",")
c1.markdown("<center> OR </center>", unsafe_allow_html=True)
ccUpload = c1.file_uploader(
    "Upload File", type=['xls', 'xlsx', 'csv', 'tsv'], key="cc")

if ccUpload is not None:
    if ccUpload.type == mimetypes.types_map['.xls'] or ccUpload.type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
        df_cc = pd.read_excel(ccUpload)
    elif ccUpload.type == mimetypes.types_map['.csv']:
        df_cc = pd.read_csv(ccUpload)
    elif ccUpload.type == mimetypes.types_map['.tsv']:
        df_cc = pd.read_csv(ccUpload, delimiter="\t")

    col = c1.selectbox("Select the Column of Mail Id's", df_cc.columns, )
    try:
        cc = df_cc[col].to_numpy().tolist()

    except:
        c1.warning("Please select the correct column for Email Id.")


bcc = c2.text_input("Bcc")
bcc = bcc.split(",")
c2.markdown("<center> OR </center>", unsafe_allow_html=True)
bccUpload = c2.file_uploader(
    "Upload File", type=['xls', 'xlsx', 'csv', 'tsv'], key="bcc")

if bccUpload is not None:
    if bccUpload.type == mimetypes.types_map['.xls'] or bccUpload.type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
        df_bcc = pd.read_excel(bccUpload)
    elif bccUpload.type == mimetypes.types_map['.csv']:
        df_bcc = pd.read_csv(bccUpload)
    elif bccUpload.type == mimetypes.types_map['.tsv']:
        df_bcc = pd.read_csv(bccUpload, delimiter="\t")

<<<<<<< HEAD
    col = c2.selectbox("Select the Column of Mail Id's", df_bcc.columns)
    try:
        bcc = df_bcc[col].to_numpy().tolist()
        print(bcc)
    except:
        c2.warning("Please select the correct column for Email Id.")

=======
>>>>>>> 31963c2eef02ca384c1efb486a4246cffbd4c1ba
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
<<<<<<< HEAD

st.info(
    """We support Markdown Editor 🎉 If you are new to Markdown check this [Guide](https://www.markdownguide.org/basic-syntax/).""")


# Attachments options for mail
attachments = st.file_uploader("Attachments:", accept_multiple_files=True)

# Calling the core Mailer Class
mailer = Mailer(mailid, passwrd, server.lower())
=======

st.info(
    """We support Markdown Editor 🎉 If you are new to Markdown check this [Guide](https://www.markdownguide.org/basic-syntax/).""")
>>>>>>> 31963c2eef02ca384c1efb486a4246cffbd4c1ba

if cc == [""]:
    cc = None


<<<<<<< HEAD
def mail():
    '''Function to send the mail'''
    print(bcc)
    print("\n\n", cc)
    mailer.send_mail(to=recipients, cc=cc, bcc=bcc, subject=subject,
                     body=body, attachments=attachments)
    with st.spinner("Sending..."):
        time.sleep(5)
        st.success("Mail sent successfully!")
=======
# Attachments options for mail
attachments = st.file_uploader("Attachments:", accept_multiple_files=True)

# Calling the core Mailer Class
mailer = Mailer(mailid, passwrd, server.lower())
>>>>>>> 31963c2eef02ca384c1efb486a4246cffbd4c1ba


st.markdown("<br>", unsafe_allow_html=True)
# Sending the mail on Button Press
st.button("Send 📮", on_click=mail)
# TODO: Handle Alert if Mail not sent successfully

# Footer
st.markdown("""
<br><br>
<center> Made with ❤️ by <a href="https://gauranshkumar.github.io/" target="_blank">Gauransh Kumar</a> in 🇮🇳 </center>
""", unsafe_allow_html=True)
