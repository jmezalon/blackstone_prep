function getCommonDirectoryPath(paths) {
  if (paths.length < 2) return paths[0].join("/");

  paths = paths.map((path) => {
    return path.split("/");
  });

  let referenceArr = paths[0];

  for (let i = 1; i < paths.length; i++) {
    for (let j = 0; j < paths[i].length; j++) {
      if (referenceArr[j] != paths[i][j]) {
        referenceArr = referenceArr.slice(0, j);
        break;
      }
    }
  }

  if (!referenceArr.length) return "";

  return referenceArr.length == 1 && referenceArr[0] == ""
    ? "/"
    : referenceArr.join("/") + "/";
}

//   __________________________________________________________________

function twoSum(numbers, target) {
  let obj = {};

  for (let i = 0; i < numbers.length; i++) {
    let pair = target - numbers[i];

    if (pair in obj) {
      return [obj[pair], i];
    } else {
      obj[numbers[i]] = i;
    }
  }

  return [];
}

//   __________________________________________________________________

function totalTime(arr) {
  let timeObj = {
    day: 0,
    hour: 0,
    minute: 0,
    second: 0,
  };

  for (let i = 0; i < arr.length; i++) {
    let time = arr[i].split(":").reverse();

    for (let j = 0; j < time.length; j++) {
      if (j == 0) {
        timeObj.second += Number(time[j]);
      }

      if (j == 1) {
        timeObj.minute += Number(time[j]);
      }

      if (j == 2) {
        timeObj.hour += Number(time[j]);
      }
    }
  }

  timeObj = processTimeObj(timeObj);

  return stringFromTimeObj(timeObj);
}

function processTimeObj(timeObj) {
  if (timeObj.second > 59) {
    timeObj.minute += Math.floor(timeObj.second / 60);
    timeObj.second %= 60;
  }

  if (timeObj.minute > 59) {
    timeObj.hour += Math.floor(timeObj.minute / 60);
    timeObj.minute %= 60;
  }

  if (timeObj.hour > 23) {
    timeObj.day += Math.floor(timeObj.hour / 24);
    timeObj.hour %= 24;
  }

  return timeObj;
}

function stringFromTimeObj(timeObj) {
  let timeArr = [];

  let timeOrder = ["day", "hour", "minute", "second"];

  for (let unit of timeOrder) {
    if (timeObj[unit] > 0) {
      timeArr.push(`${timeObj[unit]} ${pluralizeTime(unit, timeObj[unit])}`);
    }
  }

  if (timeArr.length === 0) return "0";

  return timeArr.join(", ");
}

function pluralizeTime(unit, n) {
  if (n > 1) return unit + "s";
  return unit;
}

//   __________________________________________________________________

function createPhoneNumber(numbers) {
  var format = "(xxx) xxx-xxxx";

  for (var i = 0; i < numbers.length; i++) {
    format = format.replace("x", numbers[i]);
  }

  return format;
}

//   __________________________________________________________________

const insideOut = (str) => {
  return str
    .split(" ")
    .map((x) => {
      let left = x
        .substring(0, Math.floor(x.length / 2))
        .split("")
        .reverse()
        .join("");
      let right = x
        .substring(Math.ceil(x.length / 2))
        .split("")
        .reverse()
        .join("");
      let middle = x.length % 2 ? x[Math.floor(x.length / 2)] : "";
      return left + middle + right;
    })
    .join(" ");
};

//   __________________________________________________________________

function sortArray(array) {
  const odd = array.filter((x) => x % 2).sort((a, b) => a - b);
  return array.map((x) => (x % 2 ? odd.shift() : x));
}

//   __________________________________________________________________

function numObj(s) {
  return s.map((n) => {
    return { [n]: String.fromCharCode(n) };
  });
}

//   __________________________________________________________________

function reverseNum(n) {
  let rev = 0;

  while (n) {
    rev = rev * 10 + (n % 10);
    n = Math.floor(n / 10);
  }
  return rev;
}

//   __________________________________________________________________

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

function timeConverter(timeUnit, obj) {
  let hours = timeUnit[2] || 0;
  let minutes = timeUnit[1] || 0;
  let seconds = timeUnit[0] || 0;

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

//   __________________________________________________________________

const removeDuplicateIds = (obj) => {
  let sortedKeys = Object.keys(obj).sort((a, b) => b - a);
  let referenceSet = new Set();

  for (const key of sortedKeys) {
    let selectedChars = [];

    for (let letter of obj[key]) {
      if (!referenceSet.has(letter)) {
        selectedChars.push(letter);
        referenceSet.add(letter);
      }
    }
    obj[key] = selectedChars;
  }
  return obj;
};
