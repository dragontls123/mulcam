package my.jes.web.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import my.jes.web.dao.MemberDAO;
import my.jes.web.vo.MemberVO;

@Service
public class MemberService {
	@Autowired
	MemberDAO memberDAO;

	public void memberInsert(MemberVO m) throws Exception {
		memberDAO.memberInsert(m);
	}

	public String login(MemberVO m) {
		return memberDAO.login(m);
	}
}
