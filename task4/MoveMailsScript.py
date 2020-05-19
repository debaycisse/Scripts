import win32com.client


outlook = win32com.client.Dispatch("Outlook.Application")
inbox = outlook.GetNamespace("MAPI").GetDefaultFolder(6)

for message in inbox.Items:
    if (message.UnRead == True) and (str(message.Sender) == "Givanas Admin" or str(message.SenderEmailAddress) == "admin@givanas.com"):
        destination_folder = inbox.Folders.Item("Azeez")
        # move the mail into the destination_folder
        message.Move(destination_folder)
        # Mark the move item as unread, since Move() method set unread status to false after moving a mail item to another folder or sub-folder
        destination_folder.Items[0].Unread = True

