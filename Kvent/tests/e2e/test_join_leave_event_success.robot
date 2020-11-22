*** Settings ***
Library    SeleniumLibrary
Test Teardown    Close Browser
Suite Teardown    Close Browser

*** Variables ***
${BROWSER}    chrome
${URL}    https://kventeventapplication.herokuapp.com/
${USERNAME}    testRobot
${PASSWORD}    KventTestPass12345
${EMAIL}    admin@gmail.com
${FIRSTNAME}    MR. Robert
${LASTNAME}    FERGUSON
${TEL}    0991234567
${ADDRESS}    99/10 A Street California USA

*** Test Cases ***
Test user login succeed via Django auth, join and leave the existing event.
    Login to application
    Display Kvent index page
    Check information in profile page and it should matched 

*** Keywords ***
Login to application
    Open Browser    ${URL}    ${BROWSER}
    Click Element    id:event-logo
    Page Should Contain    Login
    Wait Until Page Contains Element    id:id_username
    Input Text    id:id_username    ${USERNAME}
    Input Text    id:id_password    ${PASSWORD}
    Click Element    xpath:/html/body/div/div/div/form/div[1]/button
Display Kvent index page
    Page Should Contain    KVENT
    Page Should Contain    an online booking and appointment web-application.
