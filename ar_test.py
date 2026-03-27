import ar_master

mm = ar_master.master_flask_code()
head_details=mm.select_direct_query("select user_details.name,head_details.email from user_details,head_details where user_details.head_name=head_details.name")
print(head_details)