# The PEP 484 type hints stub file for the QtWebEngine module.
#
# Generated by SIP 5.5.0
#
# Copyright (c) 2020 Riverbank Computing Limited <info@riverbankcomputing.com>
# 
# This file is part of PyQtWebEngine.
# 
# This file may be used under the terms of the GNU General Public License
# version 3.0 as published by the Free Software Foundation and appearing in
# the file LICENSE included in the packaging of this file.  Please review the
# following information to ensure the GNU General Public License version 3.0
# requirements will be met: http://www.gnu.org/copyleft/gpl.html.
# 
# If you do not wish to use this file under the terms of the GPL version 3.0
# then you may purchase a commercial license.  For more information contact
# info@riverbankcomputing.com.
# 
# This file is provided AS IS with NO WARRANTY OF ANY KIND, INCLUDING THE
# WARRANTY OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.


import typing
import sip

from PyQt5 import QtWebEngineCore

# Support for QDate, QDateTime and QTime.
import datetime

# Convenient type aliases.
PYQT_SIGNAL = typing.Union[QtCore.pyqtSignal, QtCore.pyqtBoundSignal]
PYQT_SLOT = typing.Union[typing.Callable[..., None], QtCore.pyqtBoundSignal]

# Convenient aliases for complicated OpenGL types.
PYQT_OPENGL_ARRAY = typing.Union[typing.Sequence[int], typing.Sequence[float],
        sip.Buffer, None]
PYQT_OPENGL_BOUND_ARRAY = typing.Union[typing.Sequence[int],
        typing.Sequence[float], sip.Buffer, int, None]


class QQuickWebEngineProfile(QtCore.QObject):

    class PersistentCookiesPolicy(int): ...
    NoPersistentCookies = ... # type: 'QQuickWebEngineProfile.PersistentCookiesPolicy'
    AllowPersistentCookies = ... # type: 'QQuickWebEngineProfile.PersistentCookiesPolicy'
    ForcePersistentCookies = ... # type: 'QQuickWebEngineProfile.PersistentCookiesPolicy'

    class HttpCacheType(int): ...
    MemoryHttpCache = ... # type: 'QQuickWebEngineProfile.HttpCacheType'
    DiskHttpCache = ... # type: 'QQuickWebEngineProfile.HttpCacheType'
    NoCache = ... # type: 'QQuickWebEngineProfile.HttpCacheType'

    def __init__(self, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...

    def presentNotification(self, notification: QtWebEngineCore.QWebEngineNotification) -> None: ...
    def downloadPathChanged(self) -> None: ...
    def useForGlobalCertificateVerificationChanged(self) -> None: ...
    def clientCertificateStore(self) -> QtWebEngineCore.QWebEngineClientCertificateStore: ...
    def setDownloadPath(self, path: str) -> None: ...
    def downloadPath(self) -> str: ...
    def isUsedForGlobalCertificateVerification(self) -> bool: ...
    def setUseForGlobalCertificateVerification(self, b: bool) -> None: ...
    def spellCheckEnabledChanged(self) -> None: ...
    def spellCheckLanguagesChanged(self) -> None: ...
    def isSpellCheckEnabled(self) -> bool: ...
    def setSpellCheckEnabled(self, enabled: bool) -> None: ...
    def spellCheckLanguages(self) -> typing.List[str]: ...
    def setSpellCheckLanguages(self, languages: typing.Iterable[str]) -> None: ...
    def httpAcceptLanguageChanged(self) -> None: ...
    def httpCacheMaximumSizeChanged(self) -> None: ...
    def persistentCookiesPolicyChanged(self) -> None: ...
    def httpCacheTypeChanged(self) -> None: ...
    def httpUserAgentChanged(self) -> None: ...
    def cachePathChanged(self) -> None: ...
    def persistentStoragePathChanged(self) -> None: ...
    def offTheRecordChanged(self) -> None: ...
    def storageNameChanged(self) -> None: ...
    @staticmethod
    def defaultProfile() -> 'QQuickWebEngineProfile': ...
    def clearHttpCache(self) -> None: ...
    def removeAllUrlSchemeHandlers(self) -> None: ...
    def removeUrlSchemeHandler(self, a0: QtWebEngineCore.QWebEngineUrlSchemeHandler) -> None: ...
    def removeUrlScheme(self, scheme: typing.Union[QtCore.QByteArray, bytes, bytearray]) -> None: ...
    def installUrlSchemeHandler(self, scheme: typing.Union[QtCore.QByteArray, bytes, bytearray], a1: QtWebEngineCore.QWebEngineUrlSchemeHandler) -> None: ...
    def urlSchemeHandler(self, a0: typing.Union[QtCore.QByteArray, bytes, bytearray]) -> QtWebEngineCore.QWebEngineUrlSchemeHandler: ...
    def setRequestInterceptor(self, interceptor: QtWebEngineCore.QWebEngineUrlRequestInterceptor) -> None: ...
    def setUrlRequestInterceptor(self, interceptor: QtWebEngineCore.QWebEngineUrlRequestInterceptor) -> None: ...
    def cookieStore(self) -> QtWebEngineCore.QWebEngineCookieStore: ...
    def setHttpAcceptLanguage(self, httpAcceptLanguage: str) -> None: ...
    def httpAcceptLanguage(self) -> str: ...
    def setHttpCacheMaximumSize(self, maxSize: int) -> None: ...
    def httpCacheMaximumSize(self) -> int: ...
    def setPersistentCookiesPolicy(self, a0: 'QQuickWebEngineProfile.PersistentCookiesPolicy') -> None: ...
    def persistentCookiesPolicy(self) -> 'QQuickWebEngineProfile.PersistentCookiesPolicy': ...
    def setHttpCacheType(self, a0: 'QQuickWebEngineProfile.HttpCacheType') -> None: ...
    def httpCacheType(self) -> 'QQuickWebEngineProfile.HttpCacheType': ...
    def setHttpUserAgent(self, userAgent: str) -> None: ...
    def httpUserAgent(self) -> str: ...
    def setCachePath(self, path: str) -> None: ...
    def cachePath(self) -> str: ...
    def setPersistentStoragePath(self, path: str) -> None: ...
    def persistentStoragePath(self) -> str: ...
    def setOffTheRecord(self, offTheRecord: bool) -> None: ...
    def isOffTheRecord(self) -> bool: ...
    def setStorageName(self, name: str) -> None: ...
    def storageName(self) -> str: ...


class QQuickWebEngineScript(QtCore.QObject):

    class ScriptWorldId(int): ...
    MainWorld = ... # type: 'QQuickWebEngineScript.ScriptWorldId'
    ApplicationWorld = ... # type: 'QQuickWebEngineScript.ScriptWorldId'
    UserWorld = ... # type: 'QQuickWebEngineScript.ScriptWorldId'

    class InjectionPoint(int): ...
    Deferred = ... # type: 'QQuickWebEngineScript.InjectionPoint'
    DocumentReady = ... # type: 'QQuickWebEngineScript.InjectionPoint'
    DocumentCreation = ... # type: 'QQuickWebEngineScript.InjectionPoint'

    def __init__(self, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...

    def timerEvent(self, e: QtCore.QTimerEvent) -> None: ...
    def runOnSubframesChanged(self, on: bool) -> None: ...
    def worldIdChanged(self, scriptWorldId: 'QQuickWebEngineScript.ScriptWorldId') -> None: ...
    def injectionPointChanged(self, injectionPoint: 'QQuickWebEngineScript.InjectionPoint') -> None: ...
    def sourceCodeChanged(self, code: str) -> None: ...
    def sourceUrlChanged(self, url: QtCore.QUrl) -> None: ...
    def nameChanged(self, name: str) -> None: ...
    def setRunOnSubframes(self, on: bool) -> None: ...
    def setWorldId(self, scriptWorldId: 'QQuickWebEngineScript.ScriptWorldId') -> None: ...
    def setInjectionPoint(self, injectionPoint: 'QQuickWebEngineScript.InjectionPoint') -> None: ...
    def setSourceCode(self, code: str) -> None: ...
    def setSourceUrl(self, url: QtCore.QUrl) -> None: ...
    def setName(self, name: str) -> None: ...
    def runOnSubframes(self) -> bool: ...
    def worldId(self) -> 'QQuickWebEngineScript.ScriptWorldId': ...
    def injectionPoint(self) -> 'QQuickWebEngineScript.InjectionPoint': ...
    def sourceCode(self) -> str: ...
    def sourceUrl(self) -> QtCore.QUrl: ...
    def name(self) -> str: ...
    def toString(self) -> str: ...


class QtWebEngine(sip.simplewrapper):

    def initialize(self) -> None: ...


PYQT_WEBENGINE_VERSION = ... # type: int
PYQT_WEBENGINE_VERSION_STR = ... # type: str
