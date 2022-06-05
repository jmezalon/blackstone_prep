function totalTime(arr) {
  let timeObj = {
    day: 0,
    hour: 0,
    minute: 0,
    second: 0,
  };

  let totalTime = [0, 0, 0];

  for (const time of arr) {
    let timeArr = time.split(":").reverse();

    totalTime[0] += +timeArr[0] || 0;
    totalTime[1] += +timeArr[1] || 0;
    totalTime[2] += +timeArr[2] || 0;
  }

  timeConverter(totalTime, timeObj);

  let finalTimeAndInits = [];

  for (const time in timeObj) {
    if (timeObj[time] > 0) {
      let timeVar, initials;
      switch (time) {
        case "day":
          timeVar = " day";
          break;
        case "hour":
          timeVar = " hour";
          break;
        case "minute":
          timeVar = " minute";
          break;
        default:
          timeVar = " second";
          break;
      }
      initials =
        timeObj[time] > 1
          ? timeObj[time] + timeVar + "s"
          : timeObj[time] + timeVar;
      finalTimeAndInits.push(initials);
    }
  }
  return finalTimeAndInits.join(", ") || "0";
}

function timeConverter(totalTImeArr, obj) {
  let hours = totalTImeArr[2] || 0;
  let minutes = totalTImeArr[1] || 0;
  let seconds = totalTImeArr[0] || 0;

  getHoursToDay(hours, obj);
  getMinutesToHours(minutes, obj);
  getSecondsToMinutes(seconds, obj);

  if (obj.hour > 23) getHoursToDay(obj.hour, obj);
  if (obj.minute > 59) getMinutesToHours(obj.minute, obj);
}

function getHoursToDay(hours, obj) {
  if (hours > 0) {
    while (hours >= 0) {
      if (hours > 23) {
        obj.day += 1;
      } else {
        obj.hour = hours;
      }
      hours = hours - 24;
    }
  }
}
function getMinutesToHours(minutes, obj) {
  if (minutes > 0) {
    while (minutes >= 0) {
      if (minutes > 59) {
        obj.hour += 1;
      } else {
        obj.minute = minutes;
      }
      minutes = minutes - 60;
    }
  }
}

function getSecondsToMinutes(seconds, obj) {
  if (seconds > 0) {
    while (seconds >= 0) {
      if (seconds > 59) {
        obj.minute += 1;
      } else {
        obj.second = seconds;
      }
      seconds = seconds - 60;
    }
  }
}

console.log(
  totalTime(["24:00:00", "24:00:00", "09:88:79", "15:30:04", "07", "30"])
);
