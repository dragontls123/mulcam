$(document).ready(function() {
	$("#loginBtn").click(function() {//로그인 처리	

		var id = $("#id").val();
		var pw = $("#pw").val();

		//alert(id+":"+pw);		

		$.post("login.jes",
			{
				id: id,
				pw: pw
			},
			function(data, status) {
				var obj = JSON.parse(data);
				if (obj.name) {
					data = obj.name + "<input type='button' value='logout' id='logoutBtn' class='btn btn-primary'>";
					$.cookie("logined", data);
					$("#msgDiv").html(data);
				} else {
					alert(obj.msg);
					location.reload();
				}
			}
		);//end post() 
	});//end 로그인 처리


	$(document).on("click", "#logoutBtn", function(event) { //로그아웃 처리

		$.post("logout.jes",
			{

			},
			function(data, status) {

				$.removeCookie("logined");
				location.reload();
			}
		);//end post() 
	});//end 로그아웃 처리




	$("#memberInsertBtn").click(function() {//회원 가입 처리

		var name = $("#name").val();
		var id = $("#id").val();
		var pw = $("#pw").val();

		//alert(name+":"+id+":"+pw);

		$.post("../memberInsert.jes",
			{
				name: name,
				id: id,
				pw: pw
			},
			function(data, status) {
				alert(data);
				//$("#msgDiv", opener.document).html(data+"님 환영합니다");
				window.close();
			}
		);//end post()
	});//end 회원 가입 처리


});
