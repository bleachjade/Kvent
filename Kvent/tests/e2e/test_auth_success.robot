*** Settings ***
Library    SeleniumLibrary
Test Teardown    Close Browser
Suite Teardown    Close Browser

*** Variables ***
${BROWSER}    chrome
${URL}    https://kventeventapplication.herokuapp.com/
# you have to change the username everytime you tested because it already recorded in the database!
${USERNAME}    testAdmin9
${PASSWORD}    KventTestPass12345
${EMAIL}    admin@gmail.com
${FIRSTNAME}    MR. Robert
${LASTNAME}    FERGUSON
${TEL}    0991234567
${ADDRESS}    99/10 A Street California USA
# gmail account to use in the tests
${GOOGLE_EMAIL}    test@gmail.com
${GOOGLE_PASSWORD}    password

*** Test Cases ***
Test user sign up succeed and then login succeed via Django auth.
    Display sign up page with multiple input boxs
    Input information and sign up
    Shows login page
    Input information that you just filled in sign up page and login
    Display Kvent index page via Django auth
    Check information in profile page and it should matched 

Test user login succeed via Google auth.
    Display login page with a Google login button
    Display Google login page
    Proceed login
    Display Kvent index page via Google auth
    Check information in profile page via Google email

*** Keywords ***
# test case 1
Display sign up page with multiple input boxs
    Open Browser    ${URL}    ${BROWSER}
    Click Element    id:event-logo
    Capture Page Screenshot
    Wait Until Page Contains Element    id:id_username
    Click Element    xpath:/html/body/div/div/div/form/div[2]/p[2]/a
Input information and sign up
    Wait Until Page Contains Element    id:id_username
    Capture Page Screenshot
    Input Text    id:id_username    ${USERNAME}
    Input Text    id:id_email    ${EMAIL}
    Input Text    id:id_first_name    ${FIRSTNAME}
    Input Text    id:id_last_name    ${LASTNAME}
    Input Text    id:id_phone_num    ${TEL}
    Input Text    id:id_address    ${ADDRESS}
    Input Text    id:id_password1    ${PASSWORD}
    Input Text    id:id_password2    ${PASSWORD}
    Click Element    xpath:/html/body/div/div/div/form/div/button
Shows login page
    Page Should Contain    Login
    Capture Page Screenshot
    Wait Until Page Contains Element    id:id_username
    Capture Page Screenshot
Input information that you just filled in sign up page and login
    Input Text    id:id_username    ${USERNAME}
    Input Text    id:id_password    ${PASSWORD}
    Click Element    xpath:/html/body/div/div/div/form/div[1]/button
Display Kvent index page via Django auth
    Page Should Contain    KVENT
    Page Should Contain    an online booking and appointment web-application.
    Capture Page Screenshot
Check information in profile page and it should matched
    Click Element    xpath:/html/body/nav/ul/li[2]/a
    Wait Until Page Contains    Account Infomation
    Capture Page Screenshot
    Page Should Contain    ${FIRSTNAME}
    Page Should Contain    ${LASTNAME}
    Page Should Contain    ${ADDRESS}
    Page Should Contain    ${TEL}

# test case 2
Display login page with a Google login button
    Open Browser    ${URL}    ${BROWSER}
    Click Element    id:event-logo
    Capture Page Screenshot
    Wait Until Page Contains    Google+
    Capture Page Screenshot
    Click Element    xpath:/html/body/div/div/div/form/div[1]/a
Display Google login page
    Wait Until Page Contains Element    id:identifierId
Proceed login
    Input Text    id:identifierId    ${GOOGLE_EMAIL}
    Click Element    xpath://*[@id="identifierNext"]/div/button/div[2]
    Wait Until Page Contains Element    xpath://*[@id="password"]/div[1]/div/div[1]/input
    Page Should Contain Element    xpath://*[@id="password"]/div[1]/div/div[1]/input
    Capture Page Screenshot
    Input Text    xpath://*[@id="password"]/div[1]/div/div[1]/input    ${GOOGLE_PASSWORD}
    Click Element    xpath://*[@id="passwordNext"]/div/button/div[2]
Display Kvent index page via Google auth
    Wait Until Page Contains    KVENT
    Page Should Contain    an online booking and appointment web-application.
    Capture Page Screenshot
Check information in profile page via Google email
    Click Element    xpath:/html/body/nav/ul/li[2]/a
    Wait Until Page Contains    Account Infomation
    Capture Page Screenshot
    Page Should Contain    ${GOOGLE_EMAIL}