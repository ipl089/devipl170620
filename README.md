# Python で ユニットテスト

このリポジトリは[DevIPL/2017spring](https://github.com/DevIPL/2017spring)の発表資料です。 [GitHub Pages](https://nagayama1147.github.io/devipl170620/).

私が Python でユニットテストするときの枠組みを紹介しました。

## 説明はいい。とにかく動かしたい

PythonとGitが実行できる場合：

```console
> git clone git@github.com:nagayama1147/devipl170620.git
> rm test/testqlineedit.py
> python setup.py test
```

test/testqlineedit.py のみ、追加パッケージPyQt5に依存するため削除する。

実行は、test.bat を叩いても良い。


## 自分の環境でも使いたい

テストの枠組みの以下をコピーする。

```
+ src/                                   
  __init__.py                            
+ test/                                  
  unittest-tutorial_test.py              
setup.py                               
```

test/ に test\*.py という名前でテストファイルを作る。

テストファイルには unittest.TestCase を継承した TestCase を定義する。

test/teststr.py でいうと、以下の部分があればよい。

```python
# test/teststr.py
import unittest


class TestCase(unittest.TestCase):
    def test_upper(self):
        s = "Hello"
        self.assertEqual(s.upper(), "HELLO")
```

unittest の仕組みで、testで始まるメンバメソッド(例：testmyfunc, test\_my\_func)が、テストとして実行されるメソッド(test suite)となる。

標準パッケージ unittest の詳細については、Python のドキュメントを参考せよ。

src/ のスクリプトは、テスト実行時には直接importできるので、以下のように記述できる。

```python
# testmymath.py
import unittest
import mymath  # ../src/mymath.py


class TestCase(unittest.TestCase):
    pass
```


### テストパッケージの名前を変えたい

この仕組みでは、「unittest-tutorial」というパッケージ名でテストをしている。

これを変えたい場合、以下を対応付けるように修正する。


setup.py の引数 name と src/\_\_init\_\_.py の パッケージ名(unittest-tutorial)

```python
# setup.py
    name = "unittest-tutorial",
```

```python
# src/__init__.py
from unittest-tutorial import *
```

setup.py の引数 test\_suite の先頭部分と test/ のメインファイル名(unittest-tutorial\_test)


```python
# setup.py
    test_suite = 'unittest-tutorial_test.suite'
```

```python
# test/unittest-tutorial_test.py
```


## これはどういう仕組みなの？

Python のパッケージ作成用パッケージ setuptools を利用して、テスト向けパッケージ unittest を活用したテストを柔軟に追加できる運用を目的としている。

仕組みは標準パッケージのみで構築されている（デモ用コードにあるPyQt5は考慮しない）。

setup.py は、以下を意図している。

1. test/ から src/ の Python スクリプトを参照できるようにする
1. モジュール unittest-tutorial\_test の関数 suite を全体の test suite とする

test/unittest-tutorial\_test.py は以下を意図している。

1. test/ のファイル test\*.py をテストモジュールのスクリプトファイルとみなす
1. テストモジュールの TestCase クラスの関数 test\* を test suite に追加する

## PyQt5 のテストについて

Qt 固有の都合だが、Qt のクラスを活用するには QApplication が必要になる。

そのため、テスト全体で一つだけ QApplication を作成するため以下のコードの記載がある。


```python
from PyQt5.QtWidgets import QApplication


if QApplication.instance() is None:
    import sys
    app = QApplication(sys.argv)
```
