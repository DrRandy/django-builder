*** Settings ***

Documentation   Django Builder Robot Tests
Library         OperatingSystem      

*** Variables ***

${ROOT}           /projects/environment/home/django-builder
${PATH}           /projects/environment/home/django-builder/OUTPUT
${PROJECT_NAME}   mysite
${DIR}            ${PATH}/${PROJECT_NAME}
${SUBDIR}         ${DIR}/${PROJECT_NAME}


*** Test Cases ***

Path to project folder should be correct
    Directory Should Exist    ${ROOT}


Building a project creates a project folder
    Directory Should Exist    ${DIR}
    Directory Should Not Be Empty    ${DIR}
    Directory Should Exist    ${DIR}/${PROJECT_NAME}

The project folder should contain the correct files
    File Should Exist   ${DIR}/manage.py
    File Should Exist   ${SUBDIR}/__init__.py
    File Should Exist   ${SUBDIR}/urls.py
    FIle Should Exist   ${SUBDIR}/settings.py

  