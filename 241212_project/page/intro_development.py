import streamlit as st

def app():
    
	st.markdown("""
    
    # 개발 환경 구축
    
    ## 0. 아나콘다 켜기

    1. 아나콘다 파워 쉘 실행

    ```
    clear : 화면지우기
    ls : 파일 및 디렉토리 보여주기
    cd : 디렉토리 변경
    pwd : 현재 디렉토리 이름 출력
    mkdir : 디렉토리 만들기
    ```

    rm : 삭제명령어
    
    ```
    rm 파일이름, rm -r 디렉토리이름
    (디렉토리 안에는 파일이 없어야 됨)
    ```
    
    ## 1. 가상환경 만들기
    
    1. conda env list : 가상환경 확인하기

    2. conda create -n pweb python=3.8

       혹은, cond create -n strweb python=3.12

       conda create -n 프로젝트이름 python=3.7.4 ipython numpy matplotlib pandas scipy scikit-learn tensorflow keras

       (현재(base) 사용하는 파이썬 버전 확인 : python -V)

    3. Proceed ([y]/n)? y (답변하기)

    4. 설치후 완료 화면
    
    ```

    To activate this environment, use
    
        $ conda activate strweb
    
    To deactivate an active environment, use
    
         $ conda deactivate
        
    ```

    5. conda activate pweb : 가상환경 들어가기


    (참고 : conda deactivate : 가상환경 나오기)
    
    
    ##2. 라이브러리 설치 (가상환경 안에서 수행)

    1. pip list : 설치된 라이브러리 확인 (복잡)

    2. python 실행
    
    3. 라이브러리 설치
    
    ```
    pip install matplotlib scipy
    ```

    (matplotlib과 scipy 설치)

    4. 라이브러리 제대로 설치 되었는지 확인

    python 실행
    ```
    import matplotlib

    import scipy
    ```
    
    
    #4. 웹서버 실행

    1. app.py 파일이 있는 폴더에서 명령어 수행 (ls 했을때, app.py 파일이 보여야 한다. )

    2. streamlit run app.py : 웹서버 실행시키기

    3. control + c
    

    # streamlit 개발
    
    ## 1. 설치

    ```
    pip3 install streamlit
    ```
    
    ## 2. 실행
    ```
    import streamlit as st
    st.title('Hello World!')
    
    streamlit run app.py
    ```
    
    ## 3. 사용
    ```
    import streamlit as st
    import pandas as pd
    df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

    st.write(df)
    ```
    
    """)
    