from basic import app,db,Puppy,session

with app.app_context():
    
    ## CREATE ##
    my_puppy = Puppy('Rufus',5)
    db.session.add(my_puppy)
    db.session.commit

    ## READ ##
    all_puppies = Puppy.query.all()
    print(all_puppies)

    ## SELECT BY ID
    puppy_one = db.session.get(Puppy, 5)
    print(puppy_one.name)

    #FILTERS
    #PRODUCE SOME SQL CODE!
    puppy_frankie = Puppy.query.filter_by(name='Frankie')
    print(puppy_frankie.all())

    ############### UPDATE
    first_puppy = db.session.get(Puppy, 1)
    first_puppy.age = 10
    db.session.add(first_puppy)
    db.session.commit()

    ## delete
    second_pup = db.session.get(Puppy, 3)
    print(puppy_one.name)
    #print(second_pup.name)
    db.session.delete(second_pup)
    db.session.commit()

    #
    all_puppies = Puppy.query.all()
    print(all_puppies)