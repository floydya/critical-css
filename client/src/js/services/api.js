import axios from 'axios'


function getCookie(name) {
  var matches = document.cookie.match(new RegExp(
    `(?:^|; )${name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1')}=([^;]*)`
  ))
  return matches ? decodeURIComponent(matches[1]) : undefined
}

let headers = {
  "X-Requested-With": "XMLHttpRequest",
  "X-CSRFToken": getCookie("csrftoken"),
  'Accept-Language': window.language
}

export default () => {
  return axios.create({
    headers: headers,
  })
}
