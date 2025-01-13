import { create } from "domain";
import { get } from "http";


const url = process.env.BACKEND_URL;
console.log(url);


class ApiClient {
  constructor(url, path) {
    this.url = url;
    this.path = path;
  }

  create(data) {
    return fetch(`${this.url}/${this.path}`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    });
  }

  async read() {
    const response = await fetch(`${this.url}/${this.path}`, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    });
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    return response;
  }

  update(data) {
    return fetch(`${this.url}/${this.path}`, {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    });
  }

  delete(data) {
    return fetch(`${this.url}/${this.path}`, {
      method: "DELETE",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    });
  }
}


const createBackendClient = (path) => {
  return new ApiClient("http://localhost:8021", path);
}


export { ApiClient, createBackendClient };