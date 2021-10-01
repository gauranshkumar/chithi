
def get_server_info(server):
    server_details = {
        "Gmail": "Please allow Gmail's [Third Part Apps](http://www.google.com/settings/security/lesssecureapps) for mailing with us.",
        "Yahoo": "Please check this [guide](https://www.yahoo-helpline.com/blog/can-i-access-less-secure-apps-using-yahoo-mail/#Access_less_secure_apps_using_Yahoo_Mail) to allow Third Party Apps in Yahoo.",
        "Outlook": "If you have enabeled two-step verification on your account, then please Follow this [guide](https://support.microsoft.com/en-us/account-billing/using-app-passwords-with-apps-that-don-t-support-two-step-verification-5896ed9b-4263-e681-128a-a6f2979a7944) to Setup App Password for this app on Outlook.",
        "Hotmail": "If you have enabeled two-step verification on your account, then please Follow this [guide](https://support.microsoft.com/en-us/account-billing/using-app-passwords-with-apps-that-don-t-support-two-step-verification-5896ed9b-4263-e681-128a-a6f2979a7944) to Setup App Password for this app on Hotmail.",
        "iCloud": "Please check this [guide](https://support.apple.com/en-in/HT202304) to allow Third Party Email Client's for iCloud."

    }
    return server_details[server]
