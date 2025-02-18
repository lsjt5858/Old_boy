import http from 'k6/http';
import { check } from 'k6';

export const options = {
  // 配置压测参数（按需调整）
  vus: 3,            // 模拟10个并发用户
  duration: '3s',    // 持续运行30秒
};

export default function () {
  const url = 'http://localhost:8084/login';

  // 构造表单数据（注意密码转为字符串）
  const payload = {
    username: 'sang',
    password: '123', // K6要求表单值为字符串类型
  };

  // 发送POST请求
  const response = http.post(url, payload);

  // 验证响应结果
  check(response, {
    '状态码是200': (r) => r.status === 200,
    // '包含token字段': (r) => {
    //   try {
    //     return r.json().token !== undefined;
    //   } catch (e) {
    //     return false;
    //   }
    // }
  });

  // 调试时可取消注释（正式压测不建议）
  // console.log(JSON.stringify(response.json()));
}