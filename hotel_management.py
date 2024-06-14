import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# Simulating a database with dataframes
guests = []
rooms = {101: 'Available', 102: 'Available', 103: 'Available', 104: 'Available'}
bookings = []

def check_in(guest_name, room_number):
    if rooms[room_number] == 'Available':
        guests.append({'Guest Name': guest_name, 'Room Number': room_number, 'Check-in': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
        rooms[room_number] = 'Occupied'
        bookings.append({'Guest Name': guest_name, 'Room Number': room_number, 'Booking Date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
        st.success(f"{guest_name} has been checked into room {room_number}.")
    else:
        st.error(f"Room {room_number} is already occupied.")

def check_out(guest_name, room_number):
    global guests
    guests = [guest for guest in guests if guest['Guest Name'] != guest_name]
    rooms[room_number] = 'Available'
    st.success(f"{guest_name} has been checked out from room {room_number}.")

def display_rooms():
    st.subheader("Room Status")
    room_df = pd.DataFrame(list(rooms.items()), columns=['Room Number', 'Status'])
    st.table(room_df)

def display_guests():
    st.subheader("Current Guests")
    if guests:
        guest_df = pd.DataFrame(guests)
        st.table(guest_df)
    else:
        st.info("No guests currently checked in.")

# Streamlit layout
st.title("Hotel Management System")

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Check In", "Check Out", "View Rooms", "View Guests"])

if page == "Home":
    st.header("Welcome to the Hotel Management System")
    st.write("Use the sidebar to navigate through different options.")
    
elif page == "Check In":
    st.header("Guest Check In")
    guest_name = st.text_input("Guest Name")
    room_number = st.selectbox("Room Number", [room for room, status in rooms.items() if status == 'Available'])
    if st.button("Check In"):
        check_in(guest_name, room_number)

elif page == "Check Out":
    st.header("Guest Check Out")
    guest_name = st.text_input("Guest Name")
    room_number = st.selectbox("Room Number", [room for room, status in rooms.items() if status == 'Occupied'])
    if st.button("Check Out"):
        check_out(guest_name, room_number)

elif page == "View Rooms":
    display_rooms()

elif page == "View Guests":
    display_guests()