const datetime_stamp = document.getElementById('datetime_stamp');
initial_date = datetime_stamp.getAttribute('initial_date');
initial_time = datetime_stamp.getAttribute('initial_time');
//console.log(datetime_stamp_picker)
//console.log(initial_date)
//console.log(initial_time)

bulmaCalendar.attach(datetime_stamp, {
 	type: 'datetime',
 	dateFormat: 'yyyy/MM/dd',
 	//timeFormat: "h:mm a", // 12hr with AM/PM
 	timeFormat: "HH:mm",    // 24hr with no AM/PM 
 	startDate: initial_date,
 	startTime: initial_time,
});