//! Main binary entry point for fatcat_openapi implementation.

#![allow(missing_docs)]

use clap::{App, Arg};

mod server;

/// Create custom server, wire it to the autogenerated router,
/// and pass it to the web server.
fn main() {
    env_logger::init();

    let matches = App::new("server")
        .arg(
            Arg::with_name("https")
                .long("https")
                .help("Whether to use HTTPS or not"),
        )
        .get_matches();

    let addr = "127.0.0.1:8080";

    hyper::rt::run(server::create(addr, matches.is_present("https")));
}
