package my.jes.web.dao;

import org.apache.ibatis.session.SqlSession;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;

import my.jes.web.vo.MemberVO;

@Repository
public class MemberDAO {
	@Autowired
	SqlSession sqlSession;
	
	public void memberInsert(MemberVO m) {
		sqlSession.insert("mapper.member.memberInsert",m);
	}
	public String login(MemberVO m) {
		return sqlSession.selectOne("mapper.member.login",m);		
	}	
}

