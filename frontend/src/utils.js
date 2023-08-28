import store from "./store/store"
import axios from 'axios'


async function FetchFunction({ url, init_obj, authRequired }) {
  if (url === undefined) {
    throw Error('Url required')
  }

  if (init_obj === undefined) {
    init_obj = {}
  }

  if (authRequired === undefined) {
    var authRequired = false
  }

  if (authRequired === true) {
    if (init_obj.headers === undefined) {
      init_obj.headers = {
        'Authorization': `Bearer ${localStorage.getItem('jwt_token')}`

      }
    } else {
      init_obj.headers['Authorization'] = `Bearer ${localStorage.getItem('jwt_token')}`
    }
  }

  console.log(init_obj)

  const response = await fetch(url, init_obj).catch(() => {
    throw Error('Network Error')
  })

  if (response) {
    if (response.ok) {
      const data = await response.json().catch(() => {
        throw Error('Unexpected Response')
      })
      if (data) {
        return data
      }
    }
    else {
      let error = await response.text()
      throw new Error(error)
    }
  }
}

export default FetchFunction;
