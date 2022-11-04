# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['login.py'],
             pathex=[],
             binaries=[('driver\\chromedriver.exe', 'driver\\')],
             datas=[('user.json', '.'), ('example.ini', '.')],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts, 
          [],
          exclude_binaries=True,
          name='auto-login',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas, 
               strip=False,
               upx=True,
               upx_exclude=[],
               name='auto-login')

               
import shutil

shutil.copyfile('example.ini', '{0}/example.ini'.format(DISTPATH))
shutil.copyfile('user.json', '{0}/user.json'.format(DISTPATH))