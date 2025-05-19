Name:           inter-fonts
Version:        4.1
Release:        1%{?dist}
Summary:        Inter font family
License:        SIL OFL 1.1
URL:            https://rsms.me/inter/
Source0:        fonts
BuildArch:      noarch
Requires:       fontconfig

%description
Inter is a typeface designed for computer screens. It features a tall x-height 
to aid in readability, and it is optimized for legibility on screens.

%prep
%setup -q -c -T
cp -r %{SOURCE0} .

%install
mkdir -p %{buildroot}%{_datadir}/fonts/inter
install -m 644 fonts/Inter*.ttf %{buildroot}%{_datadir}/fonts/inter/
install -Dm 644 fonts/LICENSE.txt %{buildroot}%{_licensedir}/%{name}/LICENSE.txt

%post
fc-cache -f %{_datadir}/fonts/inter

%postun
if [ $1 -eq 0 ]; then
    fc-cache -f %{_datadir}/fonts/inter
fi

%files
%{_datadir}/fonts/inter/
%license %{_licensedir}/%{name}/LICENSE.txt

%changelog
* Mon May 19 2025 Your Name <contact@burhanverse.eu.org> - 4.1-1
- Initial RPM release of Inter font family