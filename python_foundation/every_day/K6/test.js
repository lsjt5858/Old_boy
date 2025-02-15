import http from 'k6/http';
import {check} from 'k6'



export const options = {
  vus: 1,
  duration: '3s',
}

export default function() {
    const url = 'http://localhost:8084/users'
    const data = {
        username: 'sang',
        password: '123',
    };
    // 执行 POST 请求并获取响应数据
    const res = http.post(url, JSON.stringify(data), { headers: {'Content-Type': 'application/json'}})
    // 断言返回的状态码是否为 200 并且响应时间小于 500ms
    check(res, {
        "状态吗 200":res.statusCode === 200,
        '返回的数据中包含 username': r => JSON.parse(r.body).username === 'sang',
        '返回的数据中包含 password': r => JSON.parse(r.body).password === '123',
        'response time < 500ms': r => r.timings.duration < 500,
    })
}