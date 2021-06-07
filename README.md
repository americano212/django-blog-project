# Make Blog Project use Django
------------
#### Start : 210109~
#### http://blog.pypystory.com/
------------
## 프로젝트 계획과 이유
> 그간 작게 부분부분 웹개발을 연습하다가 하나의 합쳐진 프로젝트를 만들어보고자 블로그를 개발해보고자 했다.
> 처음엔 어떤 웹 페이지를 만들어볼까 고민하다가 가장 무난하게 1인 user와 여러명의 guest들을 위한, 본인의 활동을 기록하고, 공유할 블로그를 만들어보기로 했다.
>
> 개발 기간은 넉넉하게 다음 여름방학까지 틈틈히하면서 6개월 정도로 잡고, HTML/CSS 연습 및 Django 여러 기능 구현을 하려고 한다.
> 추후 다른 기술 스택(Nodejs, React,...)들도 써보겠지만, 지금 당장 가장 손에 익은 Python 기반의 프레임워크를 선택했다.
> Python 웹 프레임워크는 크게 본인이 사용한 Django와 Flack 2개 정도가 있는데, flask는 좀 가볍게 쓰는 느낌이고, Django 커뮤니티나 자료가 더 방대하고, 기능적으로 탄탄한 것 같아서 Django 언어를 선택하게 되었다.
------------
## 참고한 책(네이버 책 링크 첨부)
> 파이썬 웹프로그래밍 실전편 Django장고를 활용한 쉽고 빠른 웹 개발
> https://book.naver.com/bookdb/book_detail.nhn?bid=15654623
>
> Do it! 점프 투 장고 파이썬 웹 개발부터 배포까지!
> https://book.naver.com/bookdb/book_detail.nhn?bid=17690511
>
> 이것이 우분투 리눅스다(개정판) 우분투 리눅스 설치부터 네트워크와 서버 구축, 운영까지
> https://book.naver.com/bookdb/book_detail.nhn?bid=16893958
------------
## 구현한 블로그 내 model 설명
------------
### [User Model]
------------
> name, nickname, phone number, birthday(YMD), BOJ ID, Codeforce ID, GitHub ID를 입력받고, User Level과 User EXP는 내부적으로 할당된다.
> 로그인, 로그아웃, 회원가입, 유저 레벨에 따른 권한부여, sql DB에 저장 등을 담당하게 된다.
> from django.contrib.auth.models import AbstractUser를 받아와서 overriding해서 Account라는 클래스를 만들었다.

------------
### [Board Model]
------------
> title, writer, slug(제목을 바탕으로 url을 만듬), description, content, create date, modify date, tags, hit
> 블로그 게시글을 담당하며, 제목, 작성자, 요약, 본문, 만든시간, 수정시간, 태그, 조회수 등을 포함한다.
> content는 from ckeditor_uploader.fields import RichTextUploadingField를 직접 사용하였다.
> CKEditor라는 모듈을 필드로 쓸 수 있어서 content 작업이 훨씬편하게 한줄로 줄어들었다.
>
> Class 형의 forms Model을 만들어서 사용하였다.
>
> Slug를 만드는 작업이 가장 까다로웠는데, 제목을 그대로 url로 변환하여 사용하는 과정에서 특수문자를 인식하지 못해 Error가 발생하는 경우였다.
> 결국 regular expression을 사용해서 특수문자를 제거하고 space를 '-'로 replace해서 해결했다.
>
> tag 기능은 from taggit.managers import TaggableManager를 가져와서 사용하였는데 큰 게시판의 tag를 만들어 두고 각각에 할당되는(게시판 제목이 태그된) 게시물들을 각 게시판에 뿌려주는 방식이다.
> 하지만 모든 게시판의 형식이 같아지는 일이 생겼는데, 프로그래밍 설계부터 잘못된 부분이라 다 갈아 엎어야해서 일단은 보류한다.
>
> 댓글 기능은 Disqus 서비스를 신청하고 HTML단에 붙여넣음으로써 구현했다. 1:N으로 따로 구현할 수도 있었겠지만 그냥 있는 서비스를 썼다.
>
------------
### [Kakao Adfit]
------------
> 카카오 광고 시스템을 넣을 수 있을까해서 Kakao Adfit을 신청하고 결과를 기다렸더니 보완사항에 대한 답변이 왔다.
> 미완성 카테고리가 있어서 보류함 + 모바일 최적화를 해야 광고를 줄 수 있음
> 추후에 해당사항들을 보완시켜보고자 한다.

------------
### 서버운영
------------
iwinv에서 우분투 리눅스 서버를 구매해서 사용하고 있으며 rCore.P2로 1core / 4GB / SSD 25GB 서버 위에서 돌아가고 있다.
외부에서 들어오는 port를 nginx 웹서버가 관리하고 있으며, Django Blog 자체는 Dockerfile로 image를 만들고, image를 build한 뒤 volume을 동기화해 가면서 운영되고 있다.
