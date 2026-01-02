def phishing_mail():
    
    message = input("Enter the email or message to check: ")
   
    words = message.lower().split()

    suspicious_words = ["urgent", "verify", "click", "account", "free", "limited"]

   
    flag = False
    for word in words:
        if word in suspicious_words:
            flag = True
            break

    if flag:
        print("⚠️ This message may be suspicious!")
    else:
        print("✅ No suspicious words detected.")


phishing_mail()
