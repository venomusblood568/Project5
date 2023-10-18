SYSTEM DESIGN
=============

-   **Course Introduction:**
    -   Learn to design and code a live streaming video app using system design principles.
    -   Targeted at beginners with little or no prior experience in system design.
-   **Large Scale Distributed Systems:**
    -   Definition: Systems intensive in compute, data, and usage.
    -   Example: Google Maps -- large data, widespread usage, frequent updates, high performance expectations.
    -   Distributed Systems: Servers distributed globally for performance and fault tolerance.
-   **Design Patterns:**
    -   Definition: Practices, principles, or processes used to build large scale distributed systems.
    -   Example: Publisher-Subscriber model for efficiently distributing content to millions of users.
-   **User Requirements and Data Definitions:**
    -   Identify core features from user requirements, e.g., seamless live streaming, user interactions.
    -   Translate features into data definitions, defining objects and their properties.
-   **APIs and Endpoints:**
    -   Define APIs for manipulating and querying data, encapsulating data as per user requirements.
    -   Design endpoints for external users to interact with the system.
-   **Engineering Requirements:**
    -   Ensure no single points of failure by spreading servers globally and within regions.
    -   Consider data duplication, partitioning, and redundancy for fault tolerance.
    -   Focus on extensibility, making features adaptable to changing requirements without extensive redesign efforts.
-   **Testing and Validation:**
    -   Test the design by running requests with various scenarios, including edge cases.
    -   Use sophisticated tools for load testing and capacity estimation to validate the system's feasibility.
-   **Recap: Designing a Live Streaming System:**
    -   Requirements: Streaming, processing, and broadcasting video, ensuring non-failure, displaying ads, allowing user reactions, displaying disclaimers/news flashes, supporting multiple devices.
    -   Key Considerations: Fault tolerance, graceful degradation of video quality, global content distribution.

* * * * *

### **System Requirements:**

1.  **Core Requirement:** The primary requirement is to stream videos to a large number of users. Streaming involves capturing video from an 8K source, storing it, and distributing it in real-time.
2.  **Additional Requirements:**
    -   Users can post comments and reactions.
    -   Ability to show a banner in case of problems.
    -   Interaction features, such as enabling musicians to communicate with the audience.
3.  **API Design:**
    -   APIs are well-defined and follow specific signatures.
    -   Example APIs: **`Get video`** for retrieving video frames, **`Post comment`** for posting comments.

### **Video Streaming:**

1.  **Video Storage:**
    -   Raw video footage is stored in a database or file system.
    -   Videos need to be stored for later querying or real-time streaming.
2.  **Streaming Optimization:**
    -   Streaming high-quality raw footage directly to mobile phones is impractical.
    -   Videos need to be processed and optimized for streaming efficiency.
3.  **APIs for Video Retrieval:**
    -   APIs like **`Get video frame`** are designed to retrieve specific frames based on user devices and offsets.
    -   Video frames are sent in chunks, and the server determines which chunks to send based on the client's context.

### **Comment System:**

1.  **Comment Storage:**
    -   Comments are stored in a database.
    -   Comments have data such as text, author ID, and video ID.
    -   Users can post comments and query existing comments for a specific video.

### **Technical Considerations:**

1.  **Network Protocols:**
    -   Use HTTP for non-real-time interactions like posting comments.
    -   Use WebRTC (peer-to-peer protocol) for real-time, efficient video streaming.
    -   WebRTC allows direct video transmission from server to client, optimizing live streaming efficiency.
2.  **Database Selection:**
    -   Consider database solutions like MySQL, Elasticsearch, Cassandra, Amazon DB, etc.
    -   Choose a database solution based on cost, speed, and scalability requirements.
3.  **Stateless Server:**
    -   Use stateless server architecture to handle requests without maintaining session context.
    -   Stateless protocols like HTTP simplify server implementation and allow easy scaling.

### **User Experience:**

1.  **Client-Side Optimization:**
    -   Clients interact with the server using specific APIs for comments and video frames.
    -   Clients specify their requirements clearly in each request.
2.  **Real-Time Behavior:**
    -   Different APIs require different behaviors.
    -   Comments can be periodically updated, while video frames need continuous real-time updates.
3.  **Efficiency and Simplicity:**
    -   Use server-side logic to handle context-based video frame requests, simplifying client-side code.
    -   Let the server handle context-related decisions to avoid duplicate requests from clients.

Please note that the provided information is a high-level overview, and actual implementation details would require more specific technical decisions, including the choice of programming languages, frameworks, and infrastructure setup. Additionally, security and error handling aspects should be thoroughly considered during the development process.

* * * * *

### **High-Level Design Considerations:**

1.  **Raw Video Handling:**
    -   Raw video footage is segmented into 10-second chunks.
    -   Various programs/processes convert these chunks into different resolutions and formats.
2.  **Storage Solutions:**
    -   Consider using well-known file systems like HDFS or video hosting solutions like Wimu.
    -   Suggested cost-effective options include Amazon S3 or other similar file systems.
3.  **Database Choices:**
    -   For comments and user data, NoSQL databases (key-value stores) are recommended over traditional SQL databases due to their scalability and flexibility.
4.  **Network Protocols:**
    -   Consider using Realtime Media Protocol (RTMP) for reliable data transfer from cameras to the database.
    -   Use protocols like WebRTC, DASH, or HLS for streaming video to end-users based on their bandwidth and device capabilities.
5.  **Content Delivery Network (CDN):**
    -   Utilize CDNs to cache static data, improving performance and reducing the load on your servers.
    -   CDNs can also help in delivering video content to users globally.

### **Low-Level Design Considerations (User-Side):**

1.  **User Actions:**

    -   Users can perform actions like play, pause, scrub, and change video quality.
    -   The system needs to remember the user's playback position for a seamless viewing experience.
2.  **Buffering and Caching:**

    -   Implement smart buffering mechanisms to preload video segments based on user behavior (e.g., pause and resume).
    -   Cache recently watched segments or videos for quick retrieval.
3.  **Optimizing Video Quality:**

    -   Adapt the video quality based on the user's device capabilities and network conditions.
    -   Allow users to switch between different resolutions for optimal viewing experience.
4.  **Concurrency and Throughput:**

    -   Address issues related to concurrency, latency, and throughput, especially in high-demand scenarios.
    -   Optimize the system for maximum throughput when dealing with video processing and delivery pipelines.
5.  **Authentication and Security:**

    -   Implement authentication mechanisms, especially when using CDNs, to control access to video content.
    -   Ensure that only authorized users can access specific content.

    * * * * *

    1.  **Continuous Pipeline Functionality:**

        -   Ensure continuous functioning of the pipeline for processing incoming videos.
        -   Quick response to new videos, assuming their importance.
        -   Context switching required for rapid response.
    2.  **Use Case Diagram:**

        -   Identify actors (admin, videographer, customer) and their actions in the system.
        -   Focus on the customer as the most important actor.
        -   Define core use cases: play video, resume from a specific timestamp, adjust video quality based on network/device, ensure non-stop play.
    3.  **Design Requirements:**

        -   Videos need metadata (description, timestamps, tags) added by admin before being added to the system.
        -   Customers should be able to play videos, resume from specific timestamps, and experience non-stop play based on network quality.
    4.  **API Design and Considerations:**

        -   Design clear APIs for actions like playing video, seeking to a specific timestamp, and buffering video frames.
        -   Consider different behaviors for similar actions based on user interaction and system requirements.
        -   Integrate events and flags for analytics and business insights, differentiating user-initiated requests from system-initiated buffering.
    5.  **Network Protocol Implementation:**

        -   Utilize adaptive protocols like S STP dash to handle bandwidth requirements.
        -   Offload bandwidth management to the protocol, ensuring seamless video delivery based on network and device capabilities.

        * * * * *

        1.  **Understanding System Design:**
            -   System design involves defining the components, modules, interfaces, and data for a system to satisfy specified requirements.
            -   It includes defining states and behaviors for objects in the system.
        2.  **Use Case Diagram:**
            -   Use case diagrams illustrate the interactions between various users and the system.
            -   Use cases represent different functionalities the system provides to its users.
            -   Users interact with the system by performing specific actions or use cases.
        3.  **Class Diagram:**
            -   Class diagrams define the states and behaviors of objects in the system.
            -   Objects have states (data) and behaviors (actions or methods).
            -   Example classes discussed: Video, User, Watched Video, Video Consuming Service.
            -   Classes have attributes (states/data) and methods (behaviors/actions).
        4.  **Sequence Diagram:**
            -   Sequence diagrams show the sequence of actions in a system.
            -   They represent how objects interact with each other over time.
            -   Sequence of actions between user, video service, and video consuming service is described.
        5.  **Key Classes and Methods:**
            -   **Video Class:**
                -   Attributes: ID, frames, metadata.
                -   Method: **`getFrame(timestamp)`** - Returns the frame for a given timestamp.
            -   **User Class:**
                -   Attributes: ID, name, email.
            -   **Watched Video Class:**
                -   Attributes: ID, videoID, userID, seekTimestamp.
                -   Method: **`getSeekTime()`** - Returns the seek time for the watched video.
            -   **Video Consuming Service Class:**
                -   Method: **`getSeekTime(watchedVideo)`** - Retrieves seek time for a watched video.
            -   **File System Class:**
                -   Method: **`getFrame(videoID, timestamp)`** - Retrieves a frame for a given video and timestamp.
        6.  **Design Considerations:**
            -   The importance of abstraction: Abstracting data and behaviors into objects simplifies code and allows for reuse.
            -   Mentioned the use of constants to avoid magic numbers in the code.
            -   Considered the flexibility of frame duration, allowing different frames to have different durations based on their content.
        7.  **Authentication and Security:**
            -   Authentication mentioned concerning video access.
            -   Discussed potential authentication challenges and decisions in the system design.
        8.  **System Design Best Practices:**
            -   Emphasized the use of diagrams (use case, class, sequence) as a reference for coding.
            -   Encouraged using established tools like Lucid for creating clear and detailed diagrams.
            -   Highlighted the importance of documentation and using diagrams to reduce thinking effort during coding.
        9.  **Additional Resources:**
            -   Mentioned additional resources and courses related to system design, including free and paid sections.
