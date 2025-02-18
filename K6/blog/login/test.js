import http from 'k6/http';
import {check} from 'k6';

export const options = {
  vus: 1,
  duration: '1s',
}

export default function() {
    const url = 'http://localhost:8084/login'
    const data = {
        username: 'sang',
        password: '123',
    };
    //url 是目标接口地址，这里是本地服务的登录接口。
    // data 是 POST 请求的请求体，包含用户名和密码。
    // 注意 POST 请求需要将 data 转为 JSON 格式的字符串，K6 要求 data 类型为字符串。
    // http.post() 函数返回一个 Response 对象，包含了 HTTP 响应头和响应体。
    // 接下来对返回的数据进行断言，验证是否符合预期。
    // check() 函数可以对 Response 对象的某些属性进行断言。
    // 断言的名称可以是任意字符串，断言的条件可以是任何 JavaScript 表达式。
    // 断言的名称和断言的条件都可以是函数，函数的返回值会作为断言的结果。
    // 注意 check() 函数的返回值是布尔值，如果断言不通过，check() 函数会抛一个 Error。
    // 最后，在 console.log() 函数中打印返回的数据，方便调试。
    // 注意：在正式压测中，不建议在 check() 函数中添加断言，因为断言会使得 K6 无法正常结束。
    // 断言的结果会在报告中打印出来，可以用来分析测试结果。
    // console.log(JSON.stringify(res.json()))
    // 执行 POST 请求并获取响应数据
    const res = http.post(url, data)

    const res_body = JSON.parse(res.body)

    // 断言返回的状态码是否为 200 并且响应时间小于 500ms
    check(res, {
        "状态吗 200": (r) => r.status === 200,
        'msg 是 "登录成功"': (r) => JSON.parse(r.body).msg === '登录成功',
        'status 是 "success"': (r) => JSON.parse(r.body).status === 'success',
        // '返回的数据中包含 username': r => JSON.parse(r.body).username === 'sang',
        // '返回的数据中包含 password': r => JSON.parse(r.body).password === '123',
        'response time < 500ms': r => r.timings.duration < 500,
    })
    console.log(JSON.stringify(res_body));
}