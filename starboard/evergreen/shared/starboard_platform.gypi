# Copyright 2016 The Cobalt Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
{
  'variables':  {
    'speech_stub_sources': [
      '<(DEPTH)/starboard/shared/stub/speech_recognizer_cancel.cc',
      '<(DEPTH)/starboard/shared/stub/speech_recognizer_create.cc',
      '<(DEPTH)/starboard/shared/stub/speech_recognizer_destroy.cc',
      '<(DEPTH)/starboard/shared/stub/speech_recognizer_is_supported.cc',
      '<(DEPTH)/starboard/shared/stub/speech_recognizer_start.cc',
      '<(DEPTH)/starboard/shared/stub/speech_recognizer_stop.cc',
      '<(DEPTH)/starboard/shared/stub/speech_synthesis_cancel.cc',
      '<(DEPTH)/starboard/shared/stub/speech_synthesis_speak.cc',
    ],
  },
}