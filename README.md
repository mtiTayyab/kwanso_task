# kwanso_task





## DB Creation
Go to **/kwanso_task** and execute below commands on shell:

    export FLASK_APP='__init__'
    flask shell
    from kwanso_task.models.user import db
    db.create_all() 

