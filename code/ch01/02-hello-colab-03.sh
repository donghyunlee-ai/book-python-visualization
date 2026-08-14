# 1. 우분투 패키지 매니저를 통해 가독성 높은 나눔 폰트를 설치합니다.
!sudo apt-get install -y fonts-nanum
# 2. 리눅스 시스템의 폰트 캐시를 갱신합니다.
!sudo fc-cache -fv
# 3. 맷플롯립이 기존에 기억하고 있던 과거의 폰트 캐시 파일을 강제로 삭제합니다.
!rm ~/.cache/matplotlib -rf
