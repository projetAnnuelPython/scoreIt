# scoreIt

Install
    .python 3.6.1
    .pip install pymysql
    .pip install tkinter
    .pip install matplotlib

Launch
    .clone project https://github.com/projetAnnuelPython/scoreIt.git
    .on your terminal, cd in your folders until you rich the project's one
    .enter python main.py

Usage

    .Login
        .enter valid credentials on login screen (email and password)
        .if you have no credentials, go to settings.json and add yourself as a user
        .all users are loaded and save to database when app launches

    .view your stats
        .on the top of the screen, are displayed your first and last names
        .on the left, you can seen a pie plot resuming your scores divided between winnings and loses
        .on the right is the users list ranked from the best score to the worst
        .on the bottom is a button that allows to go the calculations screen

    .work calculations
        . hit the button 'nouvelle opération' to display a new calculation. Note that your number of total questions is increased
        . enter your response and hit 'valider' button
        . if your answer is right, a related message text is displayed and your score is increased
        . if you're wrong, a message with the right response is displayed. Your score is updated
