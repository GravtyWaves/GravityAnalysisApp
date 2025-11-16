# ONBOARDING GUIDE - New Team Member

Welcome to GravityAnalysisApp! 🎉

## Your First Day Checklist

### 1. Read All Documentation (2-3 hours)
Read these files IN ORDER:

- [ ] `README.md` - Project overview
- [ ] `TEAM_STRUCTURE.md` - Meet your team (12 members)
- [ ] `TEAM_PROMPTS.md` - Find YOUR role's detailed prompt
- [ ] `TEAM_RULES.md` - Mandatory rules for everyone
- [ ] `CODING_STANDARDS.md` - How we write code
- [ ] `WORKFLOW.md` - Our development process

### 2. Setup Development Environment (1-2 hours)

Follow `INSTALLATION_GUIDE.md`:

```powershell
# Clone repository
git clone https://github.com/GravtyWaves/GravityAnalysisApp.git
cd GravityAnalysisApp

# Setup Python environment
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt

# Initialize database
python database/db_manager.py

# Run application
python app.py
```

### 3. Understand the Architecture (30 min)

We integrate 4 EXISTING microservices:

```
GravityAnalysisApp (Port 5000) ← This is what we build
         ↓ HTTP Requests
    ┌────┴────┬────────┬────────┐
    ↓         ↓        ↓        ↓
GravityTSE  Tech    Codal   Fundamental
(Port 5001) (5002)  (5003)   (5004)
```

**Critical**: We DON'T implement analysis algorithms. We CALL the microservices!

### 4. Run Tests (15 min)

```powershell
# All tests
pytest tests/ -v

# With coverage
pytest --cov=. --cov-report=html

# Open coverage report
Start-Process coverage_html/index.html
```

### 5. Introduce Yourself

Post in team chat:
```
Hi team! I'm [Your Name], the new [Your Role].
- Location: [Country] 🌍
- Experience: [Brief background]
- Excited about: [What you're looking forward to]
- Fun fact: [Something about you]

Ready to contribute! 🚀
```

### 6. Attend First Standup (15 min)

**Time**: 09:00 UTC daily

**Your turn** (2 min):
```
👋 Hi, I'm [Name], new [Role]
✅ Yesterday: Onboarding, setup environment
📋 Today: Read codebase, shadow [teammate]
🚫 Blockers: None yet
```

---

## Your First Week Goals

### Day 1 (Today)
- ✅ Complete onboarding checklist above
- ✅ Setup development environment
- ✅ Read all documentation
- ✅ Meet the team

### Day 2
- [ ] Shadow an experienced team member
- [ ] Review recent pull requests
- [ ] Read codebase (start with your area)
- [ ] Ask questions liberally

### Day 3
- [ ] Pick up a "good first issue" (labeled in GitHub)
- [ ] Write code, tests, documentation
- [ ] Create your first pull request
- [ ] Participate in code review

### Day 4
- [ ] Address PR feedback
- [ ] Review someone else's code
- [ ] Contribute to technical discussion
- [ ] Help with testing

### Day 5
- [ ] Attend sprint planning/review
- [ ] Reflect on first week
- [ ] Plan next week
- [ ] Celebrate! 🎉

---

## Key Contacts

| Role | Name | Nationality | Expertise |
|------|------|-------------|-----------|
| **Tech Lead** | Yuki Tanaka | 🇯🇵 Japan | Architecture, system design |
| **Backend Lead** | Elena Rodriguez | 🇪🇸 Spain | Flask, APIs, databases |
| **Microservices** | Rajesh Kumar | 🇮🇳 India | Integration, distributed systems |
| **Frontend Lead** | Sophie Laurent | 🇫🇷 France | UI, JavaScript, RTL |
| **Data Engineer** | Mohammed Al-Farsi | 🇦🇪 UAE | Data modeling, optimization |
| **Domain Expert** | Sarah Johnson | 🇺🇸 USA | Financial analysis, TSE |
| **DevOps** | Lars Andersson | 🇸🇪 Sweden | Docker, CI/CD, monitoring |
| **QA Lead** | Ana Silva | 🇧🇷 Brazil | Testing, automation |
| **Security** | Kim Min-ho | 🇰🇷 South Korea | Application security |
| **Tech Writer** | Emma O'Connor | 🇮🇪 Ireland | Documentation |
| **UX Designer** | Maria Garcia | 🇲🇽 Mexico | UI/UX, design |
| **Scrum Master** | Olga Petrov | 🇷🇺 Russia | Process, facilitation |

---

## Quick Reference

### Most Important Rules
1. **Use microservices** - Don't implement analysis yourself
2. **English code only** - All code, comments, variables
3. **Test everything** - Minimum 80% coverage
4. **Document as you code** - Docstrings mandatory
5. **Follow team decisions** - Respect democratic votes

### Code Quality Checklist
Before every commit:
- [ ] Follows coding standards
- [ ] Has unit tests (passing)
- [ ] Coverage ≥ 80%
- [ ] Documentation complete
- [ ] No hardcoded values
- [ ] Error handling present
- [ ] Self-reviewed

### Getting Help
1. Search documentation
2. Check GitHub issues
3. Ask in team chat
4. Schedule pairing session
5. Bring to standup

---

## Common Questions

**Q: I'm new to Persian/Farsi. How do I handle RTL?**
A: UI text should be Persian. Talk to Maria (UX) and Sophie (Frontend) for guidance. They have RTL templates ready.

**Q: What if I break something?**
A: Don't panic! We have tests, code review, and staging environment. Just communicate early.

**Q: How do I know what to work on?**
A: Check sprint board, look for issues labeled `good-first-issue`, or ask Olga (Scrum Master).

**Q: Can I suggest improvements?**
A: Absolutely! Create a GitHub discussion or propose in standup. Team will vote if needed.

**Q: What if I disagree with team decision?**
A: Voice your opinion during discussion, vote honestly, then respect the outcome. Democracy!

---

## Learning Resources

### Project-Specific
- GitHub: https://github.com/GravtyWaves/GravityAnalysisApp
- Microservices: Links in README.md
- API Docs: `API_DOCUMENTATION.md`

### Technology Stack
- **Flask**: https://flask.palletsprojects.com/
- **SQLAlchemy**: https://docs.sqlalchemy.org/
- **pytest**: https://docs.pytest.org/
- **Bootstrap RTL**: https://rtlcss.com/
- **Chart.js**: https://www.chartjs.org/

### Iranian Stock Market
- Tehran Stock Exchange: http://www.tse.ir/
- CODAL (reports): https://codal.ir/
- Technical Analysis: Investopedia
- Fundamental Analysis: Corporate Finance Institute

---

## Your Success = Team Success

Remember:
- **Ask questions** - There are no stupid questions
- **Be curious** - Explore and learn
- **Be humble** - Everyone is still learning
- **Be helpful** - Share what you know
- **Be patient** - Rome wasn't built in a day
- **Be collaborative** - We're a team

**Welcome aboard! Let's build something amazing together! 🚀**

---

## Next Steps

After completing this onboarding:
1. ✅ Mark this guide as read
2. 📝 Add yourself to `TEAM_STRUCTURE.md` (contact info)
3. 💬 Introduce yourself in team chat
4. 🎯 Pick your first issue from sprint board
5. 🚀 Start contributing!

Need help? Reach out to **Olga (Scrum Master)** - she's here to support you!

---

**Document Version**: 1.0.0  
**Last Updated**: 2024-11-16  
**Next Review**: Monthly
