"""
1. Disable user
    - page: /openmrs/admin/users/user.form
    - data: userId=11&retireReason=testing+only&action=Disable+Account
2. Delete user
    - page: /openmrs/admin/users/user.form
    - data: userId=11&person_id=10&person.names%5B0%5D.givenName=Test&person.names%5B0%5D.middleName=&person.names%5B0%5D.familyName=Clerk&person.gender=F&username=TestClerk&userFormPassword=XXXXXXXXXXXXXXX&confirm=XXXXXXXXXXXXXXX&roleStrings=Organizational%3A+Doctor&secretQuestion=&secretAnswer=&property=loginAttempts&value=0&property=lockoutTimestamp&value=&action=Delete+User
"""