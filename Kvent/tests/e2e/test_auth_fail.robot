*** Settings ***
Library    SeleniumLibrary
Test Teardown    Close Browser
Suite Teardown    Close Browser

*** Variables ***
${BROWSER}    chrome
${URL}    https://kventeventapplication.herokuapp.com/login
${USERNAME}    1
${PASSWORD}    1
${EMAIL}    a@a.com
${FIRSTNAME}    a
${LASTNAME}    a
${ADDRESS}    1

*** Test Cases ***
Test user sign up fail via Django auth.
    Display sign up page with multiple input boxs
    Input an error sign up information and sign up
    Reutrn the same sign up form with an error messages

Test user login fail via Django auth.
    Display login page with multiple input boxs
    Input error login info and proceed login
    Return the same login page with an error message

*** Keywords ***
Display sign up page with multiple input boxs
    Open Browser    ${URL}    ${BROWSER}
    Click Element    xpath:/html/body/div/div/div/form/div[2]/p[2]/a
Input an error sign up information and sign up
    Wait Until Page Contains Element    id:id_username
    Capture Page Screenshot
    Input Text    id:id_username    ${USERNAME}
    Input Text    id:id_email    ${EMAIL}
    Input Text    id:id_first_name    ${FIRSTNAME}
    Input Text    id:id_last_name    ${LASTNAME}
    Input Text    id:id_address    ${ADDRESS}
    Input Text    id:id_password1    ${PASSWORD}
    Input Text    id:id_password2    ${PASSWORD}
    Click Element    xpath:/html/body/div/div/div/form/div/button
Reutrn the same sign up form with an error messages
    Element Should Contain    xpath:/html/body/div/div/div/form/div/p[1]    The password is too similar to the Username.
    Element Should Contain    xpath:/html/body/div/div/div/form/div/p[2]    This password is too short. It must contain at least 8 characters.
    Element Should Contain    xpath:/html/body/div/div/div/form/div/p[3]    This password is too common.
    Element Should Contain    xpath:/html/body/div/div/div/form/div/p[4]    This password is entirely numeric.

Display login page with multiple input boxs
    Open Browser    ${URL}    ${BROWSER}
Input error login info and proceed login
    Input Text    id:id_username    ${USERNAME}
    Input Text    id:id_password    ${PASSWORD}
    Click Element    xpath:/html/body/div/div/div/form/div[1]/button
Return the same login page with an error message
    Element Should Contain    id:error1    Your username and password didn't match. Please try again.
