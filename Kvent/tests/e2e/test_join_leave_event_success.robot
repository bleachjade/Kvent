*** Settings ***
Library    SeleniumLibrary
# Test Teardown    Close Browser
# Suite Teardown    Close Browser

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
    Select and join the existing event
    Check attending event
    Leave the event

*** Keywords ***
Login to application
    Open Browser    ${URL}    ${BROWSER}
    Click Element    id:event-logo
    Capture Page Screenshot
    Wait Until Page Contains Element    id:id_username
    Input Text    id:id_username    ${USERNAME}
    Input Text    id:id_password    ${PASSWORD}
    Click Element    xpath:/html/body/div/div/div/form/div[1]/button
Display Kvent index page
    Page Should Contain    KVENT
    Page Should Contain    an online booking and appointment web-application.
    Capture Page Screenshot
Select and join the existing event
    Click Element    xpath:/html/body/section/div/div[3]/div[1]/div/a
    Wait Until Page Contains Element    id:event-name
    Page Should Contain    Date:
    Page Should Contain    Capacity:
    Page Should Contain    Host:
    Page Should Contain    Status :
    Page Should Contain    Available :
    Sleep    2s
    Click Link    xpath:/html/body/div/div[2]/a
    Sleep    2s
    Wait Until Page Contains    You've joined
    Capture Page Screenshot

Check attending event
    Click Element    xpath:/html/body/nav/ul/li[1]/a
    Page Should Contain Element    xpath:/html/body/section/div/div/div[3]/div/a/h4
    Sleep   2s
    Click Element    xpath:/html/body/section/div/div/div[3]/div/a/h4

Leave the event
    Sleep   2s
    Wait Until Page Contains Element    id:event-name
    Page Should Contain    Date:
    Page Should Contain    Capacity:
    Page Should Contain    Host:
    Click Link    xpath:/html/body/div/div[2]/a
    Sleep    2s
    Wait Until Page Contains    You've left
