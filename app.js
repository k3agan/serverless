var width = 600
var shape = {width: 300}; 
var showWidth = function() {
    document.write(this.width);
};

showWidth();

// global variable become part of the windows object, so when a function isn in the global context, we can access global variables uding the windows ojects as well as its other properties

// Creating objects with different notation:

// LITERAL NOTATION
var hotel = {}

hotel.name = 'Quay';
hotel.rooms = 40;
hotel.booked = 25;
hotel.checkAvailability = function() {
    return this.rooms - this.booked;
}

//Object Constructor Notation
var hotel = new Object();

hotel.name = 'Quary';
hotel.rooms = 40;
hotel.booked = 25;
hotel.checkAvailability = function(){
    return this.rooms - this.booked;
}

//LITERAL NOTATION
var hotel = {
    name: 'Quary',
    rooms: 40,
    booked: 25,
    checkAvailability: function(){
        return this.rooms - this.booked;
    }
}

//object Constructor Notation
function Hotel(name, rooms, booked){
    this.name = name;
    this.rooms = rooms;
    this.booked = booked;
    this.checkAvailability = function(){
        return this.rooms - this.booked;
    }
}
var quaryHotel = new Hotel("Quary", 40, 25);
var parkHotel = new Hotel('Park', 120,77);

// adding new properties to objects

quaryHotel.gym = true;
quaryHotel.pool = false;
delete quaryHotel.booked;

//writing to the document 
var elName = document.getElementById('hotelName');
elName.textContent = hotel.name;

var elPool = document.getElementById('pool');
elPool.className = hotel.pool;

var elGym = document.getElementById('gym');
elGym.className = hotel.gym;

// INDIVIDUAL OBJECTS
var hotel ={
    name: 'Quary',
    rooms: 40
}

// MULTIPLE OBJECTS
function Hotel(name, rooms){
    this.name = name;
    this.rooms = rooms;
}

var hotel1 = new Hotel('Quary',40);
var hotel2 = new Hotel('Parq', 175);
