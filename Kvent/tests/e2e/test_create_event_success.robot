*** Settings ***
Library    SeleniumLibrary
Test Teardown    Close Browser
Suite Teardown    Close Browser

*** Variables ***
${BROWSER}    chrome
${URL}    https://kventeventapplication.herokuapp.com/
${USERNAME}    testRobot
${PASSWORD}    KventTestPass12345
${EVENT-NAME}    MOCA : Art Gallery     
${SHORT-DESCRIPTION}    Best art gallery in bangkok! 
${LONG-DESCRIPTION}    The Museum of Contemporary Art is an art museum in Bangkok, Thailand. It was opened in 2012
${LOCATION}    499 Vibhavadi Rangsit Rd. Ladyao, Chatuchak, Bangkok 10900
${DATE}    2020-12-12 12:12:12
${NUMBER-OF-PEOPLE}    100

*** Test Cases ***
Test user login succeed via Django auth and create the event.
    Login to application
    Display Kvent index page
    Create the event
    Check that create event succeed

*** Keywords ***
Login to application
    Open Browser    ${URL}    ${BROWSER}
    Click Element    id:event-logo
    Sleep   2s
    Wait Until Page Contains Element    id:id_username
    Input Text    id:id_username    ${USERNAME}
    Input Text    id:id_password    ${PASSWORD}
    Click Element    xpath:/html/body/div/div/div/form/div[1]/button
Display Kvent index page
    Sleep   2s
    Wait Until Page Contains    KVENT
    Page Should Contain    an online booking and appointment web-application.
Create the event
    Sleep    2s
    Click Button    xpath:/html/body/section/div/div[3]/div[2]/a/button
    Sleep    2s
    Page Should Contain    Create Event
    Input Text    id:id_event_name    ${EVENT-NAME}
    Input Text    id:id_short_description    ${SHORT-DESCRIPTION}
    Input Text    id:id_long_description    ${LONG-DESCRIPTION}
    Input Text    id:id_location    ${LOCATION}
    Input Text    id:id_arrange_time    ${DATE}
    Input Text    id:id_number_people    ${NUMBER-OF-PEOPLE}
    Click Button    xpath:/html/body/div/div/div/form/div/button
    Sleep    2s
Check that create event succeed
    Wait Until Page Contains    ${EVENT-NAME}