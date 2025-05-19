# Inter Fonts RPM Packaging

This repository provides RPM packaging for the [Inter](https://rsms.me/inter/) font family, making it easy to install and update the Inter fonts on RPM-based Linux distributions (Fedora, CentOS, RHEL, openSUSE, etc).

## About Inter

Inter is a typeface carefully crafted & designed for computer screens. It features a tall x-height to aid in readability and is optimized for legibility on screens.

## Installation

### Using Copr (Recommended)

You can install the Inter fonts from the Copr repository (if available):

```sh
sudo dnf copr enable burhanverse/inter-fonts
sudo dnf install inter-fonts
```

### Manual RPM Build & Install

1. **Clone this repository:**
    ```sh
    git clone https://github.com/Burhanverse/inter-fonts.git
    cd inter-fonts
    ```

2. **Create the source tarball:**
    ```sh
    tar czf fonts.tar.gz fonts
    ```

3. **Build the RPM:**
    ```sh
    rpmbuild -ba inter.spec
    ```

4. **Install the RPM:**
    ```sh
    sudo dnf install ~/rpmbuild/RPMS/noarch/inter-fonts-*.rpm
    ```

## License

The Inter font family is licensed under the [SIL Open Font License 1.1](https://scripts.sil.org/OFL).

## Credits

- [Inter font by Rasmus Andersson](https://rsms.me/inter/)
- RPM packaging by [Burhanverse](mailto:contact@burhanverse.eu.org)