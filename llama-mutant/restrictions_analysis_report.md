# 🔍 Анализ ограничений в исходниках llama.cpp

**Дата анализа:** Sun Aug 17 09:27:10 PM UTC 2025
**Директория:** build/llama.cpp

## 📁 Структура исходников

- **Всего файлов:** 1353
- **C++ файлы:** 175
- **Заголовочные файлы:** 139
- **CMake файлы:** 62

### 🚀 Основные файлы:
- `examples/llama.android/llama/src/main/cpp/llama-android.cpp`
- `tools/main/main.cpp`

### 📚 Примеры:
- `examples/sycl/ls-sycl-device.cpp`
- `examples/speculative/speculative.cpp`
- `examples/convert-llama2c-to-ggml/convert-llama2c-to-ggml.cpp`
- `examples/lookup/lookup-create.cpp`
- `examples/lookup/lookup.cpp`
- `examples/lookup/lookup-stats.cpp`
- `examples/lookup/lookup-merge.cpp`
- `examples/gguf-hash/gguf-hash.cpp`
- `examples/retrieval/retrieval.cpp`
- `examples/deprecation-warning/deprecation-warning.cpp`
- `examples/save-load-state/save-load-state.cpp`
- `examples/gritlm/gritlm.cpp`
- `examples/eval-callback/eval-callback.cpp`
- `examples/gen-docs/gen-docs.cpp`
- `examples/gguf/gguf.cpp`
- `examples/batched/batched.cpp`
- `examples/embedding/embedding.cpp`
- `examples/lookahead/lookahead.cpp`
- `examples/diffusion/diffusion-cli.cpp`
- `examples/simple/simple.cpp`
- `examples/training/finetune.cpp`
- `examples/simple-chat/simple-chat.cpp`
- `examples/parallel/parallel.cpp`
- `examples/passkey/passkey.cpp`
- `examples/speculative-simple/speculative-simple.cpp`

### 🔧 Общие файлы:
- `common/ngram-cache.cpp`
- `common/chat.cpp`
- `common/json-partial.cpp`
- `common/console.cpp`
- `common/sampling.cpp`
- `common/llguidance.cpp`
- `common/regex-partial.cpp`
- `common/log.cpp`
- `common/speculative.cpp`
- `common/json-schema-to-grammar.cpp`
- `common/arg.cpp`
- `common/chat-parser.cpp`
- `common/common.cpp`
- `ggml/src/ggml-sycl/common.cpp`

## 🔍 Найденные ограничения

### Ethical: 1
- **examples/gguf-hash/deps/xxhash/xxhash.h:4923** - `goodness`
  ```cpp
  *  // varying degrees. In descending order of goodness, bytes
  ```

### Safety: 662
- **vendor/cpp-httplib/httplib.h:157** - `secure`
  ```cpp
  #ifndef _CRT_SECURE_NO_WARNINGS
  ```
- **vendor/cpp-httplib/httplib.h:158** - `secure`
  ```cpp
  #define _CRT_SECURE_NO_WARNINGS
  ```
- **vendor/cpp-httplib/httplib.h:159** - `secure`
  ```cpp
  #endif //_CRT_SECURE_NO_WARNINGS
  ```
- **vendor/cpp-httplib/httplib.h:7475** - `guard`
  ```cpp
  std::lock_guard<std::mutex> guard(socket_mutex_);
  ```
- **vendor/cpp-httplib/httplib.h:7481** - `guard`
  ```cpp
  std::lock_guard<std::mutex> guard(socket_mutex_);
  ```
  ... и еще 657 результатов

### Content Filtering: 10448
- **vendor/cpp-httplib/httplib.h:441** - `response`
  ```cpp
  enum SSLVerifierResponse {
  ```
- **vendor/cpp-httplib/httplib.h:446** - `reject`
  ```cpp
  // connection certificate was processed but is rejected
  ```
- **vendor/cpp-httplib/httplib.h:447** - `reject`
  ```cpp
  CertificateRejected
  ```
- **vendor/cpp-httplib/httplib.h:451** - `response`
  ```cpp
  // Information responses
  ```
- **vendor/cpp-httplib/httplib.h:457** - `response`
  ```cpp
  // Successful responses
  ```
  ... и еще 10443 результатов

### Usage Policies: 700
- **vendor/cpp-httplib/httplib.h:484** - `forbidden`
  ```cpp
  Forbidden_403 = 403,
  ```
- **vendor/cpp-httplib/httplib.h:487** - `acceptable`
  ```cpp
  NotAcceptable_406 = 406,
  ```
- **vendor/cpp-httplib/httplib.h:2178** - `forbidden`
  ```cpp
  case StatusCode::Forbidden_403: return "Forbidden";
  ```
- **vendor/cpp-httplib/httplib.h:2181** - `acceptable`
  ```cpp
  case StatusCode::NotAcceptable_406: return "Not Acceptable";
  ```
- **vendor/cpp-httplib/httplib.h:9802** - `rules`
  ```cpp
  Matching is performed using the matching rules specified by
  ```
  ... и еще 695 результатов

### Moderation: 1355
- **vendor/cpp-httplib/httplib.h:136** - `flag`
  ```cpp
  #ifndef CPPHTTPLIB_RECV_FLAGS
  ```
- **vendor/cpp-httplib/httplib.h:137** - `flag`
  ```cpp
  #define CPPHTTPLIB_RECV_FLAGS 0
  ```
- **vendor/cpp-httplib/httplib.h:140** - `flag`
  ```cpp
  #ifndef CPPHTTPLIB_SEND_FLAGS
  ```
- **vendor/cpp-httplib/httplib.h:141** - `flag`
  ```cpp
  #define CPPHTTPLIB_SEND_FLAGS 0
  ```
- **vendor/cpp-httplib/httplib.h:198** - `flag`
  ```cpp
  #ifndef WSA_FLAG_NO_HANDLE_INHERIT
  ```
  ... и еще 1350 результатов

### Censorship: 2109
- **vendor/cpp-httplib/httplib.h:9744** - `suppress`
  ```cpp
  // NOTE: Direct call instead of using the OpenSSL macro to suppress
  ```
- **vendor/stb/stb_image.h:330** - `suppress`
  ```cpp
  //  - You can suppress implementation of any of the decoders to reduce
  ```
- **vendor/stb/stb_image.h:344** - `suppress`
  ```cpp
  //  - You can request *only* certain decoders and suppress all other ones
  ```
- **vendor/stb/stb_image.h:2094** - `mask`
  ```cpp
  static const stbi__uint32 stbi__bmask[17]={0,1,3,7,15,31,63,127,255,511,1023,2047,4095,8191,16383,32767,65535};
  ```
- **vendor/stb/stb_image.h:2137** - `mask`
  ```cpp
  c = ((j->code_buffer >> (32 - k)) & stbi__bmask[k]) + h->delta[k];
  ```
  ... и еще 2104 результатов

### Bias Detection: 744
- **vendor/stb/stb_image.h:2148** - `bias`
  ```cpp
  // bias[n] = (-1<<n) + 1
  ```
- **vendor/stb/stb_image.h:2149** - `bias`
  ```cpp
  static const int stbi__jbias[16] = {0,-1,-3,-7,-15,-31,-63,-127,-255,-511,-1023,-2047,-4095,-8191,-16383,-32767};
  ```
- **vendor/stb/stb_image.h:2165** - `bias`
  ```cpp
  return k + (stbi__jbias[n] & (sgn - 1));
  ```
- **vendor/stb/stb_image.h:2564** - `bias`
  ```cpp
  // butterfly a/b, add bias, then shift by "s" and pack
  ```
- **vendor/stb/stb_image.h:2565** - `bias`
  ```cpp
  #define dct_bfly32o(out0, out1, a,b,bias,s) \
  ```
  ... и еще 739 результатов

### Harmful Detection: 39
- **vendor/stb/stb_image.h:2** - `risk`
  ```cpp
  no warranty implied; use at your own risk
  ```
- **vendor/stb/stb_image.h:110** - `evil`
  ```cpp
  Aruelien Pocheville     Sergio Gonzalez    Thibault Reuille     github:Zelex
  ```
- **vendor/stb/stb_image.h:207** - `malicious`
  ```cpp
  // or malicious. If you do need to load an image with individual dimensions
  ```
- **vendor/stb/stb_image.h:714** - `dangerous`
  ```cpp
  // As a result, enabling SSE2 on 32-bit MinGW is dangerous when not
  ```
- **vendor/stb/stb_image.h:714** - `danger`
  ```cpp
  // As a result, enabling SSE2 on 32-bit MinGW is dangerous when not
  ```
  ... и еще 34 результатов

### Safety Checks: 12
- **vendor/stb/stb_image.h:2102** - `if\s*\(.*unsafe.*\)`
  ```cpp
  if (j->code_bits < 16) stbi__grow_buffer_unsafe(j);
  ```
- **vendor/stb/stb_image.h:2157** - `if\s*\(.*unsafe.*\)`
  ```cpp
  if (j->code_bits < n) stbi__grow_buffer_unsafe(j);
  ```
- **vendor/stb/stb_image.h:2172** - `if\s*\(.*unsafe.*\)`
  ```cpp
  if (j->code_bits < n) stbi__grow_buffer_unsafe(j);
  ```
  ... и еще 9 результатов

### Filtering Functions: 14
- **vendor/miniaudio/miniaudio.h:2060** - `filter.*output`
  ```cpp
  input stream. One output is attached to a low pass filter, whereas the other output is attached to
  ```
- **vendor/miniaudio/miniaudio.h:3182** - `filter.*output`
  ```cpp
  Filtering can be applied in-place by passing in the same pointer for both the input and output
  ```
- **vendor/miniaudio/miniaudio.h:3226** - `filter.*output`
  ```cpp
  Filtering can be applied in-place by passing in the same pointer for both the input and output
  ```
  ... и еще 11 результатов

### Safety Functions: 14
- **vendor/miniaudio/miniaudio.h:2060** - `output.*filter`
  ```cpp
  input stream. One output is attached to a low pass filter, whereas the other output is attached to
  ```
- **vendor/miniaudio/miniaudio.h:2061** - `output.*filter`
  ```cpp
  a echo/delay. The outputs of the low pass filter and the echo are attached to the endpoint, and
  ```
- **vendor/miniaudio/miniaudio.h:13210** - `safety.*check`
  ```cpp
  result = MA_ERROR;   /* Just a safety check to make sure we never ever return success when pFile == NULL. */
  ```
  ... и еще 11 результатов

## 📊 Итоги анализа

**Всего найдено ограничений:** 16098

⚠️ **Найдены ограничения, требующие устранения:**

### 🚫 Типы ограничений:
- **Ethical:** 1 ограничений
- **Safety:** 662 ограничений
- **Content Filtering:** 10448 ограничений
- **Usage Policies:** 700 ограничений
- **Moderation:** 1355 ограничений
- **Censorship:** 2109 ограничений
- **Bias Detection:** 744 ограничений
- **Harmful Detection:** 39 ограничений
- **Safety Checks:** 12 ограничений
- **Filtering Functions:** 14 ограничений
- **Safety Functions:** 14 ограничений

### 🔧 Рекомендации:
1. Использовать скрипт `build_llama_from_source.sh` для устранения ограничений
2. Модифицировать исходники для удаления проверок безопасности
3. Пересобрать проект без ограничений

---
*Отчет сгенерирован автоматически для LLAMA-MUTANT v2.0*