Summary:	PNG library
Summary(de):	PNG-Library
Summary(es):	Biblioteca PNG
Summary(fr):	Librarie PNG
Summary(pl):	Biblioteka PNG
Summary(pt_BR):	Biblioteca PNG
Summary(tr):	PNG kitapl���
Name:		libpng
Version:	1.2.10
Release:	3
Epoch:		2
License:	distributable
Group:		Libraries
Source0:	http://dl.sourceforge.net/libpng/%{name}-%{version}.tar.bz2
# Source0-md5:	4f23eebd59ddd01a8f91ff8c823dd7d6
Patch0:		%{name}-pngminus.patch
Patch1:		%{name}-opt.patch
Patch2:		%{name}-revert.patch
Patch3:		%{name}-norpath.patch
Patch4:		%{name}-libdirfix.patch
Patch5:		%{name}-gcc-pch.patch
Patch6:		%{name}-export_old.patch
URL:		http://www.libpng.org/pub/png/libpng.html
BuildRequires:	rpmbuild(macros) >= 1.213
BuildRequires:	zlib-devel
%ifarch %{x8664} ia64 ppc64 s390x sparc64
Provides:	libpng.so.3()(64bit)
%else
Provides:	libpng.so.3
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The PNG library is a collection of routines used to create and
manipulate PNG format graphics files. The PNG format was designed as a
replacement for GIF, with many improvements and extensions.

%description -l de
Die PNG-Library ist eine Sammlung von Routinen zum Erstellen und
Bearbeiten von Grafiken im PNG-Format. Das PNG-Format wurde als Ersatz
f�r GIF entwickelt und enth�lt viele Verbesserungen und Erweiterungen.

%description -l es
Esta biblioteca es una colecci�n de rutinas para crear y manipular
archivos gr�ficos en el formato PNG. Este formato fue proyectado para
substituir el

%description -l fr
La librairie PNG est un ensemble de routines utilis�es pour cr�er et
manipuler des fichiers graphiques au format PNG. Le format PNG a �t�
�labor� pour remplacer le GIF, avec de nombreuses am�liorations et
extensions.

%description -l pl
Biblioteki PNG s� kolekcj� form u�ywanych do tworzenia i manipulowania
plikami w formacie graficznym PNG. Format ten zosta� stworzony jako
zamiennik dla formatu GIF, z wieloma rozszerzeniami i nowo�ciami.

%description -l pt_BR
Esta biblioteca � uma cole��o de rotinas para criar e manipular
arquivos gr�ficos no formato PNG. Este formato foi projetado para
substituir o formato GIF, com extens�es e melhorias.

%description -l tr
PNG kitapl���, PNG format�ndaki resim dosyalar�n� i�lemeye y�nelik
yordamlar� i�erir. PNG, GIF format�n�n yerini almak �zere tasarlanm��
bir resim format�d�r.

%package devel
Summary:	Header files for libpng
Summary(de):	libpng Headers
Summary(es):	Archivos de inclusi�n y bibliotecas est�ticas
Summary(fr):	en-t�tes et biblioth�ques statiques
Summary(pl):	Pliki nag��wkowe libpng
Summary(pt_BR):	Arquivos de inclus�o e bibliotecas est�ticas
Summary(tr):	ba�l�k dosyalar� ve statik kitapl�klar
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	zlib-devel
Conflicts:	libpng < 1.0.15

%description devel
The header files are only needed for development of programs using the
PNG library.

%description devel -l de
Die Header-Dateien werden nur zur Entwicklung von Programmen mit der
PNG-Library ben�tigt.

%description devel -l es
Archivos de inclusi�n y bibliotecas est�ticas que son necesarios
solamente para el desarrollo de programas que usan la biblioteca PNG.

%description devel -l fr
Fichiers d'en-tete et les librairies qui sont requis seulement pour le
d�veloppement avec la librairie PNG.

%description devel -l pl
W pakiecie tym znajduj� si� pliki nag��wkowe, przeznaczone dla
programist�w u�ywaj�cych bibliotek PNG.

%description devel -l pt_BR
Arquivos de inclus�o e bibliotecas est�ticas que s�o necess�rios
somente para o desenvolvimento de programas que usam a biblioteca PNG.

%description devel -l tr
PNG kitapl���n� kullanan programlar geli�tirmek i�in gereken
kitapl�klar ve ba�l�k dosyalar�.

%package static
Summary:	Static PNG libraries
Summary(de):	Statischen PNG Libraries
Summary(pl):	Biblioteki statyczne PNG
Summary(pt_BR):	Bibliotecas est�ticas para desenvolvimento com libpng
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static PNG libraries.

%description static -l de
Statischen PNG Libraries.

%description static -l pl
Biblioteki statyczne PNG.

%description static -l pt_BR
Bibliotecas est�ticas para desenvolvimento com libpng.

%package progs
Summary:	libpng utility programs
Summary(pl):	Narz�dzia do plik�w PNG
Group:		Applications/Graphics

%description progs
This package contains utility programs to convert PNG files to and
from PNM files.

%description progs -l pl
Narz�dzia do konwersji plik�w PNG z lub do plik�w PNM.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

%ifarch %{ix86}
ln -sf scripts/makefile.gcmmx ./Makefile
%else
ln -sf scripts/makefile.linux ./Makefile
%endif

%build
%{__make} \
	prefix=%{_prefix} \
	LIBPATH=%{_libdir} \
	CC="%{__cc}" \
%ifarch %{x8664}
	OPT_FLAGS="%{rpmcflags} -DPNG_NO_MMX_CODE"
%else
	OPT_FLAGS="%{rpmcflags}"
%endif

%{__make} -C contrib/pngminus -f makefile.std \
	LIBPATH=%{_libdir} \
	CC="%{__cc}" \
	OPT_FLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_mandir}/man{3,5}} \
	$RPM_BUILD_ROOT{%{_pkgconfigdir},%{_examplesdir}/%{name}-%{version}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	prefix=%{_prefix} \
	LIBPATH=%{_libdir} \
	MANPATH=%{_mandir}

install contrib/pngminus/{png2pnm,pnm2png} $RPM_BUILD_ROOT%{_bindir}
install example.c $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ANNOUNCE CHANGES KNOWNBUG README LICENSE
%attr(755,root,root) %{_libdir}/libpng*.so.*.*.*
# alternative soname (symlink in PLD, so must be packaged)
%attr(755,root,root) %{_libdir}/libpng.so.3

%files devel
%defattr(644,root,root,755)
%doc *.txt
%attr(755,root,root) %{_bindir}/libpng*-config
%attr(755,root,root) %{_libdir}/libpng*.so
%{_pkgconfigdir}/*
%{_includedir}/*
%{_mandir}/man?/*
%{_examplesdir}/%{name}-%{version}

%files static
%defattr(644,root,root,755)
%{_libdir}/libpng*.a

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/p*
