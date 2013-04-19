Summary:	WenQuanYi MicroHei TrueType fonts
Name:		fonts-ttf-wqy-microhei
Version:	0.2.0
Release:	10
License:	ASL 2.0 or GPLv3
Group:		System/Fonts/True type
Url:		http://wenq.org/
Source0:	http://freefr.dl.sourceforge.net/sourceforge/wqy/wqy-microhei-%{version}-beta.tar.gz
BuildArch:	noarch
BuildRequires:	fontconfig

%description
WenQuanYi Micro Hei font family is a Sans-Serif style (also known as Hei,
Gothic or Dotum among the Chinese/Japanese/Korean users) high quality
CJK outline font. It was derived from "Droid Sans Fallback", "Droid
Sans" and "Droid Sans Mono" released by Google Corp. This font package
contains two faces, "Micro Hei" and "Micro Hei Mono", in form of a
True-Type Collection (ttc) file. All the unified CJK Han glyphs, i.e.
GBK Hanzi, in the range of U+4E00-U+9FC3 defined in Unicode Standard 5.1
are covered, with additional support to many other international
languages such as Latin, Extended Latin, Hanguls and Kanas. The font
file is extremely compact (~5M) compared with most known CJK fonts.
As a result, it can be used for hand-held devices or embedded systems, or
used on PC with a significantly small memory footprint. Because both
font faces carry hinting and kerning instructions for Latin glyphs,
they are the excellent choices for desktop fonts.

%package -n fonts-ttf-default-zh_CN
Summary:	Virtual package providing default zh_CN fonts
Group:		System/Fonts/True type
Requires:	%{name} = %{version}

%description -n fonts-ttf-default-zh_CN
This package provides default TrueType font for zh_CN locale.

%prep
%setup -qn wqy-microhei

%build

%install
mkdir -p %{buildroot}/%{_datadir}/fonts/TTF/wqy-microhei
install -m 644 *.ttc %{buildroot}/%{_datadir}/fonts/TTF/wqy-microhei

mkdir -p %{buildroot}%{_sysconfdir}/X11/fontpath.d/
ln -s ../../..%{_datadir}/fonts/TTF/wqy-microhei \
	%{buildroot}%{_sysconfdir}/X11/fontpath.d/ttf-wqy-microhei:pri=50

%files
%doc *.txt
%dir %{_datadir}/fonts/TTF/wqy-microhei/
%{_datadir}/fonts/TTF/wqy-microhei/*.ttc
%{_sysconfdir}/X11/fontpath.d/ttf-wqy-microhei:pri=50

%files -n fonts-ttf-default-zh_CN

