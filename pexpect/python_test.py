#!/usr/bin/env python3
'''
Test with the Python REPL itself.
'''
import sys
import pexpect
prompt = '>>> '
child = pexpect.spawn('python3', encoding='utf-8')
child.setecho(False)
child.expect(prompt)
child.sendline('1 + 1')
child.expect(prompt)
assert child.before.rstrip() == '2'
child.sendline('2 + 2')
child.expect(prompt)
assert child.before.rstrip() == '4'
child.sendcontrol('d')
child.close()
