# TEAM RULES & PROTOCOL
# GravityAnalysisApp - Mandatory for ALL 12 Team Members

---

## 🎯 MISSION STATEMENT

We are building GravityAnalysisApp - a professional web-based platform for analyzing Iranian stock market using **EXISTING microservices**. Our work is collaborative, democratic, high-quality, and user-focused.

---

## ⚠️ CRITICAL RULES (NEVER VIOLATE)

### Rule #1: Use Existing Microservices
**DO**:
```python
# ✅ CORRECT - Call external microservice
response = requests.get('http://localhost:5001/api/symbols')
data = response.json()
```

**DON'T**:
```python
# ❌ WRONG - Implement analysis yourself
def calculate_rsi(prices):
    # Don't write this! Use Gravity_TechAnalysis microservice!
    pass
```

**Why**: We are INTEGRATING, not REIMPLEMENTING. The microservices already exist on GitHub.

---

### Rule #2: English Code Only
**DO**:
```python
# ✅ CORRECT
def get_symbol_price(symbol_code: str) -> float:
    """Fetch current price for symbol"""
    return price
```

**DON'T**:
```python
# ❌ WRONG
def گرفتن_قیمت_نماد(کد_نماد):  # Persian in code!
    return قیمت
```

**Why**: International collaboration, code maintainability, industry standard.

**Note**: User-facing content (UI text, documentation for users) should be in Persian/Farsi.

---

### Rule #3: Democratic Decisions
**DO**:
- Participate in all votes
- Respect majority decision (>60% or <40%)
- Accept owner vote on 40-60% splits
- Implement approved decisions without complaint

**DON'T**:
- Skip voting
- Ignore team decisions
- Argue after vote is concluded
- Implement features without approval

**Why**: Team collaboration, shared ownership, conflict resolution.

---

### Rule #4: Test Everything
**DO**:
```python
# ✅ CORRECT - Comprehensive tests
class TestMarketDataService:
    def test_get_symbols_success(self):
        """Test successful API call"""
        # Test implementation
        
    def test_get_symbols_connection_error(self):
        """Test network failure"""
        # Test error handling
        
    def test_get_symbols_timeout(self):
        """Test timeout scenario"""
        # Test timeout handling
```

**Minimum Requirements**:
- 80% code coverage
- Unit tests for all functions
- Integration tests for APIs
- Error scenario tests

**DON'T**:
```python
# ❌ WRONG - No tests
def get_symbols():
    return requests.get(url).json()
# Where are the tests?!
```

**Why**: Quality assurance, regression prevention, confidence in changes.

---

### Rule #5: Document As You Code
**DO**:
```python
# ✅ CORRECT
def calculate_eps(net_income: float, shares: int) -> float:
    """
    Calculate Earnings Per Share.
    
    Args:
        net_income: Company's net income in Rials
        shares: Number of outstanding shares
    
    Returns:
        EPS value, or 0.0 if shares is 0
    
    Raises:
        ValueError: If shares is negative
    """
    if shares < 0:
        raise ValueError("Shares cannot be negative")
    return net_income / shares if shares > 0 else 0.0
```

**DON'T**:
```python
# ❌ WRONG - No documentation
def calculate_eps(net_income, shares):
    return net_income / shares if shares > 0 else 0.0
```

**Required Documentation**:
- Docstrings for all functions/classes
- API endpoint documentation
- README updates for features
- Comments explaining WHY (not WHAT)

**Why**: Knowledge sharing, onboarding, maintenance.

---

## 📋 MANDATORY PRACTICES

### 1. Code Standards
**Read and follow**: `CODING_STANDARDS.md`

**Before every commit**:
- [ ] Follows PEP 8 (Python) or ESLint (JavaScript)
- [ ] Type hints present (Python)
- [ ] Naming conventions correct
- [ ] No hardcoded values
- [ ] Error handling complete

### 2. Git Workflow
**Branch naming**:
```bash
feature/ISSUE-123-integrate-gravitytse
bugfix/ISSUE-456-fix-chart-rendering
hotfix/ISSUE-789-security-patch
docs/ISSUE-101-update-readme
```

**Commit messages**:
```
feat(market-data): integrate GravityTSE microservice

- Replace mock data with API calls
- Add retry logic and error handling
- Include comprehensive tests

Closes #123
```

**Pull Requests**:
- Minimum 2 approvals required
- All tests must pass
- Coverage ≥ 80%
- Documentation updated

### 3. Code Review
**When reviewing**:
- [ ] Check functionality
- [ ] Verify tests exist and pass
- [ ] Confirm coding standards followed
- [ ] Validate documentation
- [ ] Check security implications
- [ ] Test error handling
- [ ] Provide constructive feedback

**Response time**:
- Critical: 2 hours
- High: 4 hours
- Normal: 24 hours

### 4. Testing
**Test pyramid**:
```
       /\
      /E2E\       ← Few critical user journeys
     /------\
    /INTEGR.\    ← API integration tests
   /----------\
  /UNIT TESTS \  ← Many fast isolated tests
 /--------------\
```

**Run before commit**:
```bash
# Unit tests
pytest tests/unit/ -v

# With coverage
pytest --cov=. --cov-report=term

# All tests
pytest tests/ -v
```

### 5. Security
**ALWAYS**:
- Validate ALL user inputs
- Use parameterized queries (SQL injection prevention)
- Sanitize outputs (XSS prevention)
- Handle errors without leaking info
- Keep dependencies updated
- Never commit secrets/API keys

**Example**:
```python
# ✅ SECURE
from sqlalchemy import text

def get_symbol(code: str):
    # Validate input
    if not re.match(r'^[آ-ی\w]{1,10}$', code):
        raise ValueError("Invalid symbol code")
    
    # Parameterized query
    result = db.execute(
        text('SELECT * FROM symbols WHERE code = :code'),
        {'code': code}
    )
    return result.fetchone()

# ❌ INSECURE
def get_symbol_bad(code):
    # SQL INJECTION VULNERABILITY!
    result = db.execute(f"SELECT * FROM symbols WHERE code = '{code}'")
    return result.fetchone()
```

---

## 🤝 COLLABORATION RULES

### Communication
1. **Be Respectful**: Every opinion matters
2. **Be Clear**: Provide context and examples
3. **Be Responsive**: Acknowledge messages within 24h
4. **Be Constructive**: Criticize ideas, not people
5. **Be Helpful**: Share knowledge freely
6. **Be Asynchronous**: Don't expect immediate responses

### Language Usage
- **Code**: English ONLY
- **Technical discussions**: English
- **User-facing content**: Persian/Farsi
- **UI text**: Persian/Farsi (RTL)

### Daily Standup (09:00 UTC, 15 min)
Each person (2 min max):
1. What did I complete yesterday?
2. What will I work on today?
3. Any blockers?

**Rules**:
- Be punctual
- Be concise
- Take detailed discussions offline
- Focus on progress, not excuses

### Code Reviews
- Review others' code within SLA
- Provide actionable feedback
- Explain your reasoning
- Acknowledge good work
- Don't be pedantic
- Focus on important issues

---

## 🗳️ DEMOCRATIC VOTING

### When to Vote
- Feature additions
- Technical decisions
- Architecture changes
- Breaking changes
- Tool/library choices

### Voting Thresholds

| Type | Threshold | Use For |
|------|-----------|---------|
| **Simple Majority** | 7+ votes | Features, minor decisions |
| **Super Majority** | 9+ votes | Architecture, major changes |
| **Unanimous** | 12 votes | Security, data loss, license |

### Owner Vote Rule
If votes split 40-60%:
- Owner gets ONE deciding vote
- Owner has 12 hours to decide
- Owner's vote is final

**Example**:
```
Vote: Implement Redis caching
Results: 5 Yes (42%), 7 No (58%)
Status: 42%-58% split → Owner vote needed
```

### After Vote
- **Approved**: Implement without further discussion
- **Rejected**: Don't implement, move on
- **Respect decision**: No complaining after vote

---

## ✅ QUALITY GATES

### Before Creating PR
- [ ] Code follows CODING_STANDARDS.md
- [ ] All tests pass locally
- [ ] Code coverage ≥ 80%
- [ ] No hardcoded values
- [ ] Error handling complete
- [ ] Documentation updated
- [ ] Self-reviewed code
- [ ] Commit messages meaningful

### Before Merging PR
- [ ] 2+ approvals received
- [ ] All CI checks pass
- [ ] No merge conflicts
- [ ] Code reviewed by relevant experts
- [ ] Security review (if needed)
- [ ] Performance acceptable

### Before Deployment
- [ ] All tests pass
- [ ] QA tested
- [ ] Documentation published
- [ ] Changelog updated
- [ ] Team notified
- [ ] Rollback plan ready

---

## 🚨 ESCALATION PROCEDURES

### When Stuck (Blocker)
1. Try to solve yourself (30 min)
2. Search documentation/Google (30 min)
3. Ask team member with expertise (1 hour)
4. Raise in daily standup
5. Schedule focused discussion
6. Escalate to Tech Lead if critical

### When Disagreement
1. Discuss with person directly
2. Present both viewpoints
3. Involve Tech Lead/Scrum Master
4. Create vote if needed
5. Accept decision
6. Move forward

### Production Incident
1. Create incident channel immediately
2. Notify team (Slack/Discord)
3. Assess severity (P0-P3)
4. Assign incident commander
5. Fix or rollback
6. Post-mortem meeting
7. Document lessons learned

---

## 📊 PERFORMANCE METRICS

### Individual
- Code quality (review feedback)
- Test coverage of your code
- PR review turnaround time
- Bugs introduced
- Documentation completeness
- Team collaboration

### Team
- Sprint velocity
- Code coverage (80%+ target)
- Bug rate (< 5% target)
- Deployment frequency
- Mean time to recovery
- User satisfaction

---

## 🎓 CONTINUOUS LEARNING

### Expectations
- Stay updated on technologies
- Learn from code reviews
- Share knowledge with team
- Attend technical discussions
- Read documentation
- Improve skills continuously

### Knowledge Sharing
- Write technical blog posts
- Present in team meetings
- Create tutorials
- Update documentation
- Mentor junior members
- Share useful resources

---

## 🏆 TEAM VALUES

### Quality Over Speed
- Do it right the first time
- Test thoroughly
- Review carefully
- Refactor when needed
- Don't rush

### Collaboration Over Competition
- Help teammates
- Share credit
- Celebrate together
- Learn from each other
- No heroes, only team

### Transparency Over Secrecy
- Share information openly
- Document decisions
- Communicate proactively
- Admit mistakes
- Ask for help

### Simplicity Over Complexity
- Write simple code
- Use simple solutions
- Avoid over-engineering
- Keep it maintainable
- YAGNI (You Aren't Gonna Need It)

---

## 📖 REQUIRED READING

Every team member MUST read:
1. ✅ `TEAM_STRUCTURE.md` - Team roles and responsibilities
2. ✅ `TEAM_PROMPTS.md` - Your role-specific prompt
3. ✅ `CODING_STANDARDS.md` - How to write code
4. ✅ `WORKFLOW.md` - Development workflow
5. ✅ `THIS FILE` - Team rules (you're reading it!)

Optional but recommended:
- `README.md` - Project overview
- `API_DOCUMENTATION.md` - API reference
- `INSTALLATION_GUIDE.md` - Setup instructions

---

## ❓ FREQUENTLY ASKED QUESTIONS

### Q: Can I use a different coding style?
**A**: No. Follow CODING_STANDARDS.md strictly. Consistency > personal preference.

### Q: What if I disagree with a team decision?
**A**: Voice your concern during discussion, vote honestly, then respect the outcome.

### Q: Can I skip tests for a small change?
**A**: No. ALL code needs tests. No exceptions.

### Q: What if the microservice is down?
**A**: Implement proper error handling, show user-friendly message, log error, don't crash.

### Q: Can I add a new library?
**A**: Create a proposal, explain why, team votes (Simple Majority needed).

### Q: How do I handle urgent production bug?
**A**: Follow hotfix procedure in WORKFLOW.md, create hotfix branch, fix, test, deploy, backport.

### Q: What if I'm going to miss a deadline?
**A**: Communicate early! Raise in standup, discuss options, ask for help.

### Q: Can I work on features not in sprint?
**A**: No. Focus on committed sprint work. Propose for next sprint.

---

## 🎯 SUCCESS CRITERIA

### You're Doing Great If:
- ✅ Your code passes review on first try
- ✅ Your tests catch bugs before production
- ✅ Your documentation helps others
- ✅ Your PRs are small and focused
- ✅ You help teammates proactively
- ✅ You meet sprint commitments
- ✅ You follow all rules without reminders

### You Need Improvement If:
- ❌ Code reviews request multiple changes
- ❌ Tests are missing or inadequate
- ❌ Documentation is incomplete
- ❌ PRs are huge and complex
- ❌ You work in isolation
- ❌ You miss deadlines repeatedly
- ❌ You violate team rules

---

## 📞 WHO TO ASK

| Question About | Ask |
|---------------|-----|
| Architecture | Yuki (Tech Lead) |
| Backend code | Elena (Backend Lead) |
| Microservices | Rajesh (Integration) |
| Frontend/UI | Sophie (Frontend) / Maria (UX) |
| Database | Mohammed (Data Engineer) |
| Testing | Ana (QA Lead) |
| Security | Kim (Security) |
| DevOps | Lars (DevOps) |
| Documentation | Emma (Tech Writer) |
| Process | Olga (Scrum Master) |
| Financial domain | Sarah (Domain Expert) |
| Git/Commits | Carlos (Git Workflow Manager) |

---

## 🔄 AUTOMATED GIT WORKFLOW

### Git Workflow Manager - Carlos Mendes

**Automatic Monitoring**:
- Repository scanned every 30 minutes
- Alert triggered when uncommitted changes exceed 50 files
- Automatic categorization and commit organization
- Follows Conventional Commits standard strictly

**What Happens When Changes > 50 Files**:
1. ⚠️ Alert notification sent to team
2. 📂 Files categorized into logical groups:
   - Database layer
   - Services layer
   - Templates/UI
   - Configuration
   - Documentation
   - Tests
   - Scripts
   - Core application
3. 📝 Separate commit created for each category
4. ✅ All commits follow Conventional Commits format
5. 🚀 Automatic push to GitHub
6. 📢 Team notification with summary

**Conventional Commits Format**:
```
<type>(<scope>): <subject>

Types: feat, fix, docs, style, refactor, test, chore, perf, ci
Scopes: database, services, ui, api, config, tests, docs, setup

Examples:
feat(database): Add database layer with SQLite manager
fix(services): Fix timeout handling in microservice calls
docs(team): Add comprehensive team documentation
test(api): Add integration tests for endpoints
chore(setup): Update project configuration
```

**Your Responsibility**:
- Write code, don't worry about commits
- When you have >50 changed files, Carlos handles it
- Focus on quality code, not Git organization
- Trust the automated workflow

**Benefits**:
- ✅ Clean Git history always
- ✅ No bulk commits
- ✅ Logical categorization
- ✅ Easy to track changes
- ✅ Easy to revert if needed
- ✅ No work lost

---

## 🚀 FINAL WORDS

**Remember**:
1. We're a TEAM - collaborate, don't compete
2. QUALITY matters - do it right
3. USERS come first - build what helps them
4. RESPECT each other - be kind and professional
5. LEARN constantly - improve every day

**Our Goal**: Build the best Iranian stock market analysis platform by integrating existing microservices with excellence.

**Our Values**: Quality, Collaboration, Transparency, Simplicity

**Our Commitment**: Follow these rules, support each other, deliver great software

---

**Version**: 1.0.0  
**Effective Date**: 2024-11-16  
**Mandatory for**: ALL 13 team members  
**Review Frequency**: Monthly  
**Maintained by**: Scrum Master (Olga Petrov)

---

## ✍️ ACKNOWLEDGMENT

By working on this project, you acknowledge that you have:
- ✅ Read and understood all team rules
- ✅ Read TEAM_STRUCTURE.md, TEAM_PROMPTS.md, CODING_STANDARDS.md, WORKFLOW.md
- ✅ Committed to following these rules
- ✅ Agreed to democratic decision-making
- ✅ Understood your responsibilities
- ✅ Accepted team values

**Welcome to GravityAnalysisApp Team! Let's build something amazing together! 🚀**
