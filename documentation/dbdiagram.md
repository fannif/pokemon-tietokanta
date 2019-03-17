### Tietokantakaavion luonnos:
- User((pk) id:Integer, username:String, email:String)
- Individual((pk) id:Integer, (fk) user_id -> User, (fk) species_id -> Species, nickname:String, level:Integer, caught:Date, favourite:Boolean)
- Species((pk) id:Integer, name:String, description:String, legendary:Boolean)
- Type((pk) id:Integer, name:String)
- SpeciesType((fk) species_id -> Species, (fk) type_id -> Type)
